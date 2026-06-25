# number_1 = int(input("Enter first Number:"))
# number_2 = int(input("Enter second Number:"))

# print("1.addition")
# print("2.subtraction")
# print("3.multiply")
# print("4.division")
# print("5.square")

# choose_number = int(input("enter your choose (1-5):"))

# if choose_number==1:
#     print(f"addition:{number_1+number_2}")
# elif choose_number==2 :
#     print(f"subtraction:{number_1-number_2}")
# elif choose_number==3 :
#     print(f"multiply:{number_1*number_2}")
# elif choose_number==4 :
#     print(f"division:{number_1/number_2}")
# elif choose_number==5 :
#     print(f"square:{number_1**number_2}")
# else :
#     print("invalid number")

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 30, 40, 50]
# z = [5, 4, 3, 2, 1]

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.bar(x, y, z)

# ax.set_xlabel("X Axis")
# ax.set_ylabel("Y Axis")
# ax.set_zlabel("Z Axis")

# plt.show()

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # X, Y positions
# x = [1, 2, 3, 4, 5]
# y = [1, 1, 1, 1, 1]

# # Z positions (start from 0)
# z = [0, 0, 0, 0, 0]

# # Width, Depth, Height
# dx = [0.5] * 5
# dy = [0.5] * 5
# dz = [10, 20, 15, 25, 18]

# ax.bar3d(x, y, z, dx, dy, dz)

# ax.set_xlabel('X Axis')
# ax.set_ylabel('Y Axis')
# ax.set_zlabel('Height')
# ax.set_title('3D Bar Chart')

# plt.show()

import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111, projection='3d')

# x = [1, 2, 3, 4]
# y = [1, 1, 1, 1]
# z = [0, 0, 0, 0]

# dx = [0.5, 0.5, 0.5, 0.5]
# dy = [0.5, 0.5, 0.5, 0.5]
# dz = [10, 15, 7, 20]

# ax.bar3d(x, y, z, dx, dy, dz)

# ax.set_xlabel("X Axis")
# ax.set_ylabel("Y Axis")
# ax.set_zlabel("Height")

# plt.show()

