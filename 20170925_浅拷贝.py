# coding  = utf-8
""
"深浅拷贝针对的对象：可变的对象"
"浅拷贝：不会拷贝数据中的子对象(切片，copy),拷贝深度很浅因此子对象引用，如果原对象的子对象改变，浅拷贝的子对象ID改变；" \
"深拷贝：deepcopy，拷贝深度深，拷贝包括子对象的所有对象，因此不管原对象的子对象或对象改变，深拷贝对象或子对象不受影响"
