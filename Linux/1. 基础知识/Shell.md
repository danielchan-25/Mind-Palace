# 语法

```shell
# 基本语法
if [ command ];then
    符合该条件执行的语句
fi

# 扩展语法
if [ command ];then
    符合该条件执行的语句
elif [ command ];then
    符合该条件执行的语句
else
    符合该条件执行的语句
fi
```
**注意**
1. `[ ]` 表示条件测试。注意这里的空格很重要。要注意在'[' 后面和 ']'前面都必须要有空格
2. 注意 if 判断中对于变量的处理，需要加引号，以免一些不必要的错误。没有加双引号会在一些含空格等的字符串变量判断的时候产生错误。比如 `[ -n "$var" ]` 如果 `var` 为空会出错
3. 如果只单独使用 > 或者 < 号，系统会认为是输出或者输入重定向，虽然结果显示正确，但是其实是错误的，因此要对这些符号进行转意

## 文件/目录判断
```shell
[ -a FILE ] 如果 FILE 存在则为真。
[ -d FILE ] 如果 FILE 存在且是一个目录则返回为真。
[ -e FILE ] 如果 指定的文件或目录存在时返回为真。
[ -f FILE ] 如果 FILE 存在且是一个普通文件则返回为真。
[ -r FILE ] 如果 FILE 存在且是可读的则返回为真。
[ -w FILE ] 如果 FILE 存在且是可写的则返回为真。（一个目录为了它的内容被访问必然是可执行的）
[ -x FILE ] 如果 FILE 存在且是可执行的则返回为真。
```
## 字符串判断
```shell
[ -z STRING ] 如果STRING的长度为零则返回为真，即空是真
[ -n STRING ] 如果STRING的长度非零则返回为真，即非空是真
[ STRING1 ]　 如果字符串不为空则返回为真,与-n类似
[ STRING1 == STRING2 ] 如果两个字符串相同则返回为真
[ STRING1 != STRING2 ] 如果字符串不相同则返回为真
[ STRING1 < STRING2 ] 如果 “STRING1”字典排序在“STRING2”前面则返回为真。
[ STRING1 > STRING2 ] 如果 “STRING1”字典排序在“STRING2”后面则返回为真。
```
## 数值判断
```shell
[ INT1 -eq INT2 ] INT1和INT2两数相等返回为真 ,=
[ INT1 -ne INT2 ] INT1和INT2两数不等返回为真 ,<>
[ INT1 -gt INT2 ] INT1大于INT2返回为真 ,>
[ INT1 -ge INT2 ] INT1大于等于INT2返回为真,>=
[ INT1 -lt INT2 ] INT1小于INT2返回为真 ,<
[ INT1 -le INT2 ] INT1小于等于INT2返回为真,<=
```

# 运算

| 操作符 | 含义                           |
| ------ | ------------------------------ |
| -eq    | 等于（equal）                  |
| -ne    | 不等于（not equal）            |
| -ge    | 大于或等于（greater or equal） |
| -le    | 小于或等于（less or equal）    |
| -gt    | 大于（greater than）           |
| -lt    | 小于（less than）              |