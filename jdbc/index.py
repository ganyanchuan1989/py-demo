from modal import Person

# 创建表，如果存在不会重复创建
Person.create_table()

# insert
Person(name="ggg", sex="1", age=12).save()

# query get 返回查询结果集中的第一个
p = Person.get((Person.name == "ggg") & (Person.sex == "1"))
print(p.name, p.sex, p.age)
