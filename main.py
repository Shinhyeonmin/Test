import os
import requests
import shutil
from multiprocessing import Pool
import argparse
from collect import CollectLinks

class Sites:
    GOOGLE = 1
    NAVER = 2
    GOOGLE_FULL = 3
    NAVER_FULL = 4

    @staticmethod
    def get_text(code):
        if code == Sites.GOOGLE:
            return 'google'
        elif code == Sites.NAVER:
            return 'naver'
        elif code == Sites.GOOGLE_FULL:
            return 'google'
        elif code == Sites.NAVER_FULL:
            return 'naver'

    @staticmethod
    def get_face_url(code):
        if code == Sites.GOOGLE or Sites.GOOGLE_FULL:
            return "&tbs=itp:face"
        if code == Sites.NAVER or Sites.NAVER_FULL:
            return "&face=1"

class AutoCrawler:
    def __init__(self, skip_already_exist=True, n_threads=4,do_google=True, do_Naver=True, download_path='download',
                 full_resolution = False, face = False):

        self.skip =skip_already_exist
        self.n_threads=n_threads
        self.do_google = do_google
        self.do_naver = do_Naver
        self.download_path=download_path
        self.full_resolution = full_resolution
        self.face=face
        os.makedirs('./{}'.format(self.download_path),exist_ok=True)
    @staticmethod
    def all_dirs(path):
        paths = []
        for dir in os.listdir(path):
            if os.path.isdir(path+'/'+dir):
                paths.append(path+'/'+dir)
            return paths

    @staticmethod
    def all_files(path):
        paths=[]
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.isfile(path+'/'+file):
                    paths.append(path+'/'+file)
        return paths

    @staticmethod
    def get_extension_from_link(link,default='jpg'):
        splits = str(link).spilt('.')
        if len(splits) == 0:
            return default
        ext = splits[-1].lower()
        if ext == 'jpg' or ext == 'jpeg':
            return 'jpg'
        elif ext == 'gif':
            return 'gif'
        elif ext == 'png':
            return 'png'
        else:
            return default
    @staticmethod
    def make_dir(dirname):
        current_path = os.getcwd()
        path = os.path.join(current_path,dirname)
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def get_keywords(keywords_file='keywords.txt'):
        with open(keywords_file,'r',encoding='utf-8-sig') as f:
            text = f.read()

            lines =text.split('\n')
            lines = filter(lambda  x: x != ''and x is not None,lines)
            keywords = sorted(set(lines))

        print('{} keywords found: {}'.format(len(keywords),keywords))

        with open(keywords_file, 'w+',encoding='utf-8') as f:
            for keyword in keywords:
                f.write('{}\n'.format(keyword))
            return keywords

    def save_image_to_file(self,image,file_path):
        try:
            with open('{}'.format(file_path),'wb') as file:
                shutil.copyfileobj(image.raw, file)
        except Exception as e:
            print('Save failed - {}'.format(e))

    def download_images(self,keyword,links,site_name):
        self.make_dir('{}/{}'.format(self.download_path,keyword))
        total = len(links)
        for index, link in enumerate(links):
            try:
                print('Downloading {} from {}: {} / {}'.format(keyword,site_name,index +1,total))
                response = requests.get(link,stream =True)
                self.save_image_to_file(response,'{}/{}/{}_{}.{}'.format(self.download_path,keyword,site_name,str(index).zfill(4),ext))
                del response
            except Exception as e:
                print('Download failed -',e)
                continue

    def download_from_site(self,keyword,site_code):
        site_name=Sites.get_text(site_code)
        print('site name',site_name)
        add_url = Sites.get_face_url(site_code) if self.face else ""
        print('url',add_url)
        collect=CollectLinks()
        print('collection end')
        try:
            print('Cpllecting links... {} from {}'.format(keyword, site_name))
            if site_code == Sites.GOOGLE:
                links = collect.google(keyword, add_url)
            elif site_code == Sites.NAVER:
                links = collect.naver(keyword, add_url)
            elif site_code == Sites.GOOGLE_FULL:
                links = collect.google_full(keyword, add_url)
            elif site_code == Sites.NAVER_FULL:
                links = collect.naver_full(keyword, add_url)
            else:
                print('Invalid Site Code')
                links = []

            print('Downloading images from collected links... {} from {}'.format(keyword, site_name))
            self.download_images(keyword, links, site_name)

            print('Done {} : {}'. format(site_name, keyword))
        except Exception as e:
            print('Exception {}:{} - {}'.format(site_name, keyword,e))
    def download(self, args):
        print("download")
        self.download_from_site(keyword=args[0],site_code=args[1])

    def do_crawling(self):
        keywords = self.get_keywords()
        tasks = []
        for keyword in keywords:
            dir_name = '{}/{}'.format(self.download_path, keyword)
            if os.path.exists(os.path.join(os.getcwd(), dir_name)) and self.skip:
                print('Skipping already existing directory {}'.format(dir_name))
                continue
            if self.do_google:
                if self.full_resolution:
                    tasks.append([keyword, Sites.GOOGLE_FULL])
                else:
                    tasks.append([keyword, Sites.GOOGLE])

            if self.do_naver:
                if self.full_resolution:
                    tasks.append([keyword, Sites.NAVER_FULL])
                else:
                    tasks.append([keyword, Sites.NAVER])

        print('tasks', tasks)
        pool = Pool(self.n_threads)
        pool.map_async(self.download, tasks)
        pool.close()
        pool.join()
        print('Task ended. Pool join.')
        self.imbalance_check()
        print('End Program')

    def imbalance_check(self):
        print('Data imbalance checking...')
        dict_num_files = {}
        for dir in self.all_dirs(self.download_path):
            n_files = len(self.all_files(dir))
            dict_num_files[dir] = n_files
        avg = 0
        for dir, n_files in dict_num_files.items():
            avg += n_files / len(dict_num_files)
            print('dir: {}, file_count: {}'.format(dir, n_files))
        dict_too_small = {}
        for dir, n_files in dict_num_files.items():
            if n_files < avg * 0.5:
                dict_too_small[dir] = n_files
        if len(dict_too_small) >= 1:
            for dir, n_files in dict_too_small.items():
                print('Data imbalance detected.')
                print('Below keywords have smaller than 50% of average file count.')
                print('I recommend you to remove these directories and re-download for that keyword.')
                print('_________________________________')
                print('Too small file count directories:')
                print('dir: {}, file_count: {}'.format(dir, n_files))

            print("Remove directories above? (y/n)")
            answer = input()
            if answer == 'y':
                # removing directories too small files
                print("Removing too small file count directories...")
                for dir, n_files in dict_too_small.items():
                    shutil.rmtree(dir)
                    print('Removed {}'.format(dir))
                print('Now re-run this program to re-download removed files. (with skip_already_exist=True)')
        else:
            print('Data imbalance not detected.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--skip', type=str, default='true',
                            help='Skips keyword already downloaded before. This is needed when re-downloading.')
    parser.add_argument('--threads', type=int, default=4, help='Number of threads to download.')
    parser.add_argument('--google', type=str, default='true', help='Download from google.com (boolean)')
    parser.add_argument('--naver', type=str, default='true', help='Download from naver.com (boolean)')
    parser.add_argument('--full', type=str, default='True',
                            help='Download full resolution image instead of thumbnails (slow)')
    parser.add_argument('--face', type=str, default='False', help='Face search mode')
    args = parser.parse_args()

    _skip = False if str(args.skip).lower() == 'false' else True
    _threads = args.threads
    _google = False if str(args.google).lower() == 'false' else True
    _naver = False if str(args.naver).lower() == 'false' else True
    _full = False if str(args.full).lower() == 'false' else True
    _face = False if str(args.face).lower() == 'false' else True

    print('Options - skip:{}, threads:{}, google:{}, naver:{}, full_resolution:{}, face:{}'.format(_skip, _threads,
                                                                                                       _google, _naver,
                                                                                                       _full, _face))

    crawler = AutoCrawler(skip_already_exist=_skip, n_threads=_threads, do_google=_google, do_Naver=_naver,
                              full_resolution=_full, face=_face)
    crawler.do_crawling()
