import os
#名片列表
cards_list = []

def write_cards():
    f = open("D:\py\coding\demo\cards_list\cards_list.txt","w")
    f = write(str(cards_list))
    f.close()

def read_cards():
    is_exist = os.path.exists("D:\py\coding\demo\cards_list\cards_list.txt")
    if is_exist:
        f = open("D:\py\coding\demo\cards_list\cards_list.txt","r")
        global cards_list
        cards_list = eval(f.read())
        f.close()
    else:
        f = open("D:\py\coding\demo\cards_list\cards_list.txt","w")
        f.close()
    print(is_exist)

def show_menu():
    print("*"*50)
    print("欢迎使用名片管理系统 v1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")

def create_card():
    print("功能:新建名片")
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ：")
    email = input("请输入邮箱：")
    card_info = {"name":name,"phone":phone,"qq":qq,"email":email}
    cards_list.append(card_info)
    print("添加%s的名片成功" % name)

def show_cards():
    print("显示全部")
    if not len(cards_list):
        print("没有名片")
        return
    print("name".ljust(14),"phone".ljust(14),"qq".ljust(14),"email".ljust(14),sep="")
    print("*"*56)
    for card in cards_list:
        print(card["name"].ljust(14),card["phone"].ljust(14),card["qq"].ljust(14),card["email"].ljust(14),sep="")
    print()

def search_card():
    print("查询名片")
    name = input("请输入查询的名字：")
    for card in cards_list:
        if name== card["name"]:
            print()
            print("name".ljust(14), "phone".ljust(14), "qq".ljust(14), "email".ljust(14), sep="")
            print("*" * 56)
            print(card["name"].ljust(14), card["phone"].ljust(14), card["qq"].ljust(14), card["email"].ljust(14),
                  sep="")
            print()

def set_card():
    while True:
        menu = input("请输入对名片的操作：1.修改 2.删除 0.返回")
        if menu == "1":
            name = input("请输入姓名:")
            phone = input("请输入电话:")
            qq = input("请输入qq号:")
            email = input("请输入邮箱:")
            card["name"] = name
            card["phone"] = phone
            card["qq"] = qq
            card["email"] = email
            print("%s 的名片修改成功" % name)
            return
        elif menu == "2":
            card_info_all.remove(card)
            print("删除名片成功")
            return
        elif menu == "0":
            return
        else:
            print("输入有误，请重新输入")



