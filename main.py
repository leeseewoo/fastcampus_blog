import os
import csv
from post import Post


# file path
file_path = './data.csv'

#
post_list = []

if os.path.exists(file_path):
    #
    print('Loading...')
    f = open(file_path, 'r', encoding='utf8')
    reader = csv.reader(f)
    for data in reader:
        # print(type(data))
        # Create Post Instance
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)

else:
    #
    f = open(file_path, 'w', encoding='utf8', newline='')
    f.close()

#


def write_post():
    """  """
    print('\n\n - 게시글 쓰기 -')
    title = input('제목을 입력하세요\n>>>')
    content = input('내용을 입력하세요\n>>>')
    #
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print('게시글이 등록되었습니다.')


def list_post():
    """"""
    print('\n\n - 게시글 목록 -')
    id_list = []
    for post in post_list:
        print('번호: ', post.get_id())
        print('제목: ', post.get_title())
        print('조회수: ', post.get_view_count())
        print('')
        id_list.append(post.get_id())

    while True:
        print('Q) 글 번호를 선택하세요(메뉴로 돌아가려면 -1을 입력하세요')
        try:
            id = int(input('>>>'))
            if id in id_list:
                print('게시글 상세보기')
            elif id == -1:
                break
            else:
                print('없는 글번호입니다.')
        except ValueError:
            print('숫자를 입력하세요')


while True:
    print('\n\n - FASTCAMPUS BLOG - ')
    print('- 메뉴를 선택해 주세요 -')
    print('1. 게시글 쓰기')
    print('2. 게시글 목록')
    print('3. 프로그램 종료')
    try:
        choice = int(input('>>>'))
    except ValueError:
        print('숫자를 입력하세요')
    else:
        if choice == 1:
            # print('게시글 쓰기')
            write_post()
        elif choice == 2:
            # print('게시글 목록')
            list_post()
        elif choice == 3:
            print('프로그램 종료')
            break
