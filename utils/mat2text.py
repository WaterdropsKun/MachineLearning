import scipy.io as sio

import os


def mat2txt(file_path, key):
    count = 0
    file_list = os.listdir(file_path)
    for file in file_list:
        old_dir = os.path.join(file_path, file)
        # print(old_dir)

        # 过滤文件夹
        if os.path.isdir(old_dir):
            continue
        # 过滤非mat文件
        if os.path.splitext(file)[1] != ".mat":
            continue

        try:
            file_name = os.path.splitext(file)[0]
            file_type = ".txt"
            new_dir = os.path.join(file_path, file_name + file_type)
            # print(new_dir)

            # 读取mat文件
            mat_data = sio.loadmat(old_dir)
            # print(mat_data[key])

            # 写入txt文件
            for i in range(mat_data[key].shape[0]):
                txt_data = ""
                for j in range(mat_data[key].shape[1]):
                    data = mat_data[key][i][j]
                    txt_data += (str(data) + " ")
                # print(txt_data)
                with open(new_dir, 'a') as f:
                    f.write(txt_data + '\n')

            count = count + 1
        except Exception as e:
            print(e + file)
        else:
            pass

        print(count)

#61225
# mat2txt("./Resource/landmarks/AFW", "pts_2d") # 5207
# mat2txt("./Resource/landmarks/HELEN", "pts_2d") # 37676
# mat2txt("./Resource/landmarks/IBUG", "pts_2d") # 1786
# mat2txt("./Resource/landmarks/LFPW", "pts_2d") # 16556

# mat2txt("./Resource/pos/AFW", "Pose_Para") # 5207
# mat2txt("./Resource/pos/HELEN", "Pose_Para") # 37676
# mat2txt("./Resource/pos/IBUG", "Pose_Para") # 1786
mat2txt("./Resource/pos/LFPW", "Pose_Para") # 16556
