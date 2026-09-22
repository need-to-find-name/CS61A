# CS61A

自学 UC Berkeley [CS61A: Structure and Interpretation of Computer Programs](https://cs61a.org/) 的记录。使用 2026 spring 的课程材料，看 recording 自学。

hw / lab / disc / project 全部动手写，进度随提交记录推进。

## 进度

| 模块 | 已完成 |
|---|---|
| disc | disc1、disc2 |
| homework | hw01、hw02 |
| lab | lab00、lab01、lab02 |
| projects | hog（optional problem 12 待补）、calculator |

## 环境

用 [uv](https://docs.astral.sh/uv/) 管理，Python 版本记录在 `.python-version`。

```bash
uv sync
```

## 跑作业

课程用 `ok` 自动评分器，每个作业目录里都带一份：

```bash
cd lab/lab01
uv run python ok --local
```

`--local` 表示只在本地跑测试、不提交到 okpy。

## 目录

```
disc/                 discussion 练习
homework/             hw 作业
lab/                  lab 实验
projects/             project（hog、calculator）
independent files/    零散练习
```

## 说明

这是个人学习记录，不是教学材料。

CS61A 的课程政策不允许把解答公开张贴（原文：「Do not post your solutions online publicly ...
public repositories on Github (you are welcome to use private repositories)」，且学期结束后同样适用），
因此本仓库保持 private。
