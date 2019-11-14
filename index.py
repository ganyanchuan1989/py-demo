from modal import ComDy

# 创建表，如果存在不会重复创建
ComDy.create_table()

dy = ComDy(tags="xx", user_id="xx", v_url="xx", user_url="xx", size=12211)
print(dy.save())
