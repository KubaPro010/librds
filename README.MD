# LibRDS
LibRDS is a simple library that you can use to generate the RDS groups, just the groups, so something like `3000 2000 7575 7575` the origins of development of this started on 12 May, later creating the [rdPy](https://github.com/KubaPro010/rdPy) repository, here it is mostly similiar code but improved and packaged as a library

Example code:
```python
import librds

basic = librds
print(basic)

print(librds.GroupGenerator.ps(basic,"hi",0))
```

Output:
```
    Group(a=12288, b=0, c=0, d=0, is_version_b=None)
    Group(a=12288, b=8, c=57549, d=26729, is_version_b=False)
```