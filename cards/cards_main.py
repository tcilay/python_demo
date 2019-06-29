import cards_tool
# 主业务逻辑
cards_tool.read_cards()


# 1.显示用户主界面
while True:
    cards_tool.show_menu()
    menu_str = input("请选择执行的操作:")
    print("您选择的功能:%s" % menu_str)
    if menu_str == "1":
        cards_tool.create_card()
    elif menu_str == "2":
        cards_tool.show_cards()
    elif menu_str == "3":
        cards_tool.search_card()
    elif menu_str == "0":
        cards_tool.write_cards()
        break
    else:
        print("输入有误，请重新输入")
