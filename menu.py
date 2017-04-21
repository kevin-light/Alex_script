# menu = {
#     '北京':{
#         '海淀':{
#             '五道口':{
#                 'soho':{},
#                 '网易':{},
#                 'google':{}
#             },
#             '中关村':{
#                 '爱奇艺':{},
#                 '汽车之家':{},
#                 'youku':{},
#             },
#             '上地':{
#                 '百度':{},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '老男孩':{},
#                 '北航':{},
#             },
#             '天通苑':{},
#             '回龙观':{},
#         },
#         '朝阳':{},
#         '东城':{},
#     },
#     '上海':{
#         '闵行':{
#             "人民广场":{
#                 '炸鸡店':{}
#             }
#         },
#         '闸北':{
#             '火车战':{
#                 '携程':{}
#             }
#         },
#         '浦东':{},
#     },
#     '山东':{},
# }
#
# # exit_flag = False
# # current_layer = menu
# # layers = [menu]
# # while not exit_flag:
# #     for k in current_layer:
# #         print(k)
# #     choice = input("choice >>")
# #     if choice == 'b':
# #         current_layer = layers[-1]
# #         layers.pop()
# #     elif choice not in current_layer:continue
# #     else:
# #         layers.append(current_layer)
# #         current_layer = current_layer[choice]
#
# for i in menu:
#     print(i)
#
# exit_flag = False
#
# for j in range(3):
#     choice = input("choice >>")
#     if choice in menu:
#         a = menu[choice]
#         for choice_city in a[choice]:
#             choice_city = choice_city
#         print(choice_city)
#         while not exit_flag:
#             choice_city_one = input("choice_city_one >>")
#             if choice_city_one in choice_city:
#                 choice_city_ones = choice_city[choice_city_one]
#                 print(choice_city_one)
#             else:
#                 print("choice %s is shout not exit01" % choice_city_one)
#
#     else:
#         print("choice %s is shout not exit" % choice)
# else:
#     print("times out")
#









################################################
# Task Name: 三级菜单                           #
# Description：打印省、市、县三级菜单             #
#              可返回上一级                      #
#               可随时退出程序                   #
#----------------------------------------------#
# Author：Oliver Lee                           #
################################################

zone = {
    '山东' : {
        '青岛' : ['四方','黄岛','崂山','李沧','城阳'],
        '济南' : ['历城','槐荫','高新','长青','章丘'],
        '烟台' : ['龙口','莱山','牟平','蓬莱','招远']
    },
    '江苏' : {
        '苏州' : ['沧浪','相城','平江','吴中','昆山'],
        '南京' : ['白下','秦淮','浦口','栖霞','江宁'],
        '无锡' : ['崇安','南长','北塘','锡山','江阴']
    },
    '浙江' : {
        '杭州' : ['西湖','江干','下城','上城','滨江'],
        '宁波' : ['海曙','江东','江北','镇海','余姚'],
        '温州' : ['鹿城','龙湾','乐清','瑞安','永嘉']
    },
    '安徽' : {
        '合肥' : ['蜀山','庐阳','包河','经开','新站'],
        '芜湖' : ['镜湖','鸠江','无为','三山','南陵'],
        '蚌埠' : ['蚌山','龙子湖','淮上','怀远','固镇']
    },
    '广东' : {
        '深圳' : ['罗湖','福田','南山','宝安','布吉'],
        '广州' : ['天河','珠海','越秀','白云','黄埔'],
        '东莞' : ['莞城','长安','虎门','万江','大朗']
    }
}

province_list = list(zone.keys())
while True:
    print("省".center(50, '*'))
    for province in province_list:
        print(province_list.index(province)+1,province)

    province_number = input("province number,或输入b(back)返回上级菜单，或输入q(quit)退出：>>>")
    if province_number.isdigit():
        province_number = int(province_number)
        if 1 <= province_number <= len(province_list):
            province_name = province_list[province_number-1]
            city_list = list(zone[province_name].keys())
            while True:
                print("市".center(50,"*"))
                for city in city_list:
                    print(city_list.index(city)+1,city)
                city_number = input("please input city number ,或输入b(back)返回上级菜单，或输入q(quit)退出>>>")
                if city_number.isdigit():
                    city_number = int(city_number)
                    if 0 <= city_number <= len(city_list):
                        city_name = city_list[city_number-1]

                        county_list = zone[province_name][city_name]
                        while True:
                            print("县".center(50, "*"))
                            for county in county_list:
                                print(county_list.index(county)+1,county)
                            county_number = input('county number is,或输入b(back)返回上级菜单，或输入q(quit)退出：>>>')
                            # if county_number.isdigit():
                            #     county_number = int(county_number)
                            #     if 0 <= county_number <= len(county_list):
                            #         county_name = county_list[county_number - 1]
                            #         print(county_number,county_name)
                            #     else:
                            #         break_or_quit = input("输入b(back)返回上级菜单，或输入q(quit)退出：>>")
                            if county_number == 'b':
                                break
                            elif county_number == 'q':
                                exit()
                            else:
                                print("shuru非法")
                    else:
                        print("city number 非法")
                elif city_number == 'b':
                    break
                elif city_number == 'q':
                    exit()
        else:
            print("city number 非法")
    elif province_number == 'b':
        break
    elif province_number == 'q':
        exit()











#
# zone = {
#     '山东' : {
#         '青岛' : ['四方','黄岛','崂山','李沧','城阳'],
#         '济南' : ['历城','槐荫','高新','长青','章丘'],
#         '烟台' : ['龙口','莱山','牟平','蓬莱','招远']
#     },
#     '江苏' : {
#         '苏州' : ['沧浪','相城','平江','吴中','昆山'],
#         '南京' : ['白下','秦淮','浦口','栖霞','江宁'],
#         '无锡' : ['崇安','南长','北塘','锡山','江阴']
#     },
#     '浙江' : {
#         '杭州' : ['西湖','江干','下城','上城','滨江'],
#         '宁波' : ['海曙','江东','江北','镇海','余姚'],
#         '温州' : ['鹿城','龙湾','乐清','瑞安','永嘉']
#     },
#     '安徽' : {
#         '合肥' : ['蜀山','庐阳','包河','经开','新站'],
#         '芜湖' : ['镜湖','鸠江','无为','三山','南陵'],
#         '蚌埠' : ['蚌山','龙子湖','淮上','怀远','固镇']
#     },
#     '广东' : {
#         '深圳' : ['罗湖','福田','南山','宝安','布吉'],
#         '广州' : ['天河','珠海','越秀','白云','黄埔'],
#         '东莞' : ['莞城','长安','虎门','万江','大朗']
#     }
# }
# province_list = list(zone.keys())             #省列表
# # flag = False
# # flag1 = False
# while True:
#     print(" 省 ".center(50,'*'))
#     for i in province_list:
#         print(province_list.index(i)+1,i)       #打印省列表
#     pro_id = input("请输入省编号,或输入q(quit)退出：")   #省ID
#     if pro_id.isdigit():
#         pro_id = int(pro_id)
#         if pro_id > 0 and pro_id <= len(province_list):
#             pro_name = province_list[pro_id-1]     #根据省ID获取省名称
#             city_list = list(zone[pro_name].keys())    #根据省名称获取对应的值，从新字典中获取key，即市列表
#             while True:
#                 print(" 市 ".center(50,'*'))
#                 for v in city_list:
#                     print(city_list.index(v)+1,v)       #打印市列表
#                 city_id = input("请输入市编号,或输入b(back)返回上级菜单，或输入q(quit)退出：")
#                 if city_id.isdigit():
#                     city_id = int(city_id)
#                     if city_id > 0 and city_id <= len(city_list):
#                         city_name = city_list[city_id-1]    #根据市ID获取市名称
#                         town_list = zone[pro_name][city_name]   #根据省名称获取对应的值，从新字典中获取值，即县列表
#                         while True:
#                             print(" 县 ".center(50,'*'))
#                             for j in town_list:
#                                 print(town_list.index(j)+1,j)
#                             back_or_quit = input("输入b(back)返回上级菜单，或输入q(quit)退出：")
#                             if back_or_quit == 'b':
#                                 break                #终止此层while循环，跳转到上一层While。
#                             elif back_or_quit == 'q':
#                                # flag1 = True
#                                # break               #根据标志位结束程序。
#                                 exit()
#                             else:
#                                 print("输入非法！")
#                     else:
#                         print("编号%d不存在。"%city_id)
#                 elif city_id == 'b':
#                     break
#                 elif city_id == 'q':
#                     # flag = True
#                     # break
#                     exit()
#                 else:
#                     print("输入非法!")
#                 # if flag1:
#                 #     break
#         else:
#             print("编号%d不存在。"%pro_id)
#     elif pro_id == 'q':
#         break
#     else:
#         print("输入非法!")
#     # if flag or flag1:
#     #     break



#
# china_map = {"华南": {
#     "广东": ["广州市", "佛山市", "深圳市", "东莞市"],
#
#     "广西": ["南宁市", "柳州市", "桂林市", "北海市"],
#
#     "海南": ["海口市", "三亚市", "三沙市", "儋州市"]
#
# }, "华东": {"上海": ["黄浦区", "卢湾区", "徐汇区", "长宁区", "普陀区"],
#
#     "安徽": ["合肥市", "芜湖市", "淮南市", "马鞍山市"],
#
#     "江苏": ["南京市", "无锡市", "徐州市", "常州市", "苏州市"]
#
# }, "华北": {"北京": ["东城区", "西城区", "朝阳区", "丰台区", "石景山区", "海淀区"],
#
#     "山西": ["太原市", "大同市", "阳泉市", "长治市"],
#
#     "河北": ["石家庄市", "唐山市", "秦皇岛市", "邢台市"]
#
# }, "华中": {"湖北": ["武汉市", "黄石市", "十堰市", "十堰市"],
#
#     "河南": ["郑州市", "开封市", "洛阳市", "平顶山市"],
#
#     "湖南": ["长沙市", "株洲市", "衡阳市", "邵阳市"]
#
# }, "西南": {"重庆": ["万州区", "涪陵区", "渝中区", "大渡口区"], "四川": ["成都市", "自贡市", "攀枝花市", "德阳市"], "贵州": ["贵阳市", "六盘水市", "遵义市", "安顺市"],
#
# }, "特别行政区": {"香港": ["屯门", "弯仔", "北角", "西贡"], "澳门": ["花地玛堂区", "圣安多尼堂区", "大堂区", "望德堂区"],
#
# },
#
# }
#
# print("-------------------------------------------------")
# print("+            +")
# print("+            +")
# print("+   欢迎来到大中华地区查询系统地   +")
# print("+            +")
# print("+            +")
# print("-------------------------------------------------")
# print("大中华地区一级划分:")
# for i in china_map:  # 遍历字典的key，列出大中华地区的名字
#
#     print(i)
# print("-------------------------------------------------")
# jump_flag = False  # 用于跳出外循环
# for i in range(3):  # 外循环，指定循环3次，3次外循环完了，就退出程序
#     greater_china_name = input("请输入你要查看的大中华地区名字:")
#     if greater_china_name in china_map:  # 检查输入的地区是否在地图中，如果地区名字3次输入错误，程序退出
#         gc_name = china_map[greater_china_name]
#         province_name = gc_name.keys()  # 使用输入的信息作为key，取出省信息，存在字典中
#         while True:  # 内循环，死循环，不指定循环次数，通过break或者flag跳出
#             print("------------------包含的省名字二级:-----------------")  # 分隔线
#             for i in province_name:  # 遍历列表，取出省名字，打印出来
#                 print(i)
#             print("-------------------------------------------------")  # 分隔线
#             sheng_name_input = input("请输入你要查看的省名字:")
#
#             if sheng_name_input in province_name:  # 判断输入的省名字是否在地区列表中
#                 shi_name = china_map[greater_china_name][sheng_name_input]  # 取出省中有哪些市，存在列表中
#                 print("--------------包含的城市名三级:-------------------")  # 分隔线
#                 for i in shi_name:  # 遍历列表，取出地区市名字，打印出来
#                     print(i)
#                 print("------------------------------------------------")  # 分隔线
#
#             if sheng_name_input not in province_name:  # 如果输入的省名字不在在地区列表中
#                 print("输入的省名字不对，请重新输入")
#                 continue  # 跳出当次迭代，开始下一次迭代循环，直到地市名字输入正确为止(不停的要求输入)
#             back_or_quit = input("请问是否退出？按b:Back是返回上一级菜单;按q:Exit是退出整个程序")
#             # 显示完地区市后，就要退出程序了，一个是全部退出，一个是返回上一级菜单
#             if back_or_quit == "q":
#                 jump_flag = True  # 用于跳出外循环
#                 break  # 跳出while内循环
#             if back_or_quit == "b":
#                 continue  # 跳出当次迭代，开始下一次迭代循环,重新输入省处，返回上一步
#             print("你输入的信息有误，请重新输入")
#         if jump_flag:  # 跳出外循环的条件满足
#             break  # 跳出外循环
# else:  # 上面的3次for循环正常执行完毕，else才会执行，如果是不正常退出（break），else不会执行
#     print("3次输入错误，程序退出")
