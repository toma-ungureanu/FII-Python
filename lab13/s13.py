import os
import sqlite3
import zipfile


#
# def create_archive(a_path, ext, full_path=None):
#     print(full_path)
#     zip_file = zipfile.ZipFile("the.zip", "w", zipfile.ZIP_DEFLATED)
#     for dirpath, dirs, files in os.walk(a_path):
#         for file in files:
#             if os.path.splitext(file)[1] == ext:
#                 if full_path:
#                     zip_file.write(os.path.join(full_path, file))
#                 else:
#                     zip_file.write(os.path.join(dirpath, file))
#
#
#
# def check_archive(a_path):
#     lista = []
#     if zipfile.is_zipfile(a_path):
#         archive = zipfile.ZipFile(a_path, 'r')
#         for file in archive.infolist():
#             lista.append(file.filename)
#         print(lista)
#     else:
#         return False
#
# def add_info(a_path, db_path):
#     sqlite3.connect()
#
# # create_archive(r"C:\Users\thomi\PycharmProjects\lab13\texts", ".txt")
# # check_archive(r'C:\Users\thomi\PycharmProjects\lab13\the.zip')


def problema1(path, low, high):
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(dirpath, file)
            if not zipfile.is_zipfile(full_path):
                continue
            archive = zipfile.ZipFile(os.path.join(dirpath, file), 'r')
            for info in archive.infolist():
                if not os.path.splitext(info.filename)[1] == '.db':
                    continue
                conn = sqlite3.connect(info.filename)
                cursor = conn.cursor()
                select = '''SELECT a.title, t.name, g.name FROM tracks t 
                JOIN genres g ON t.GenreId=g.GenreId JOIN albums a ON t.AlbumId=a.AlbumId
                WHERE t.Milliseconds BETWEEN {} and {} ORDER BY a.title, t.name, g.name ASC
                '''.format(low, high)
                cursor.execute(select)
                records = cursor.fetchall()
                cursor.close()
                conn.close()
                return records


print(problema1(r"data\test1", 330000, 330200))
