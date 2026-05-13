import pandas as pd
data={
    "企業":["A社","B社","C社","D社"],
    "PER":[12,25,8,15],
    "ROE":[14,5,18,10],
    "自己資本比率":[55,30,70,45]
}
df=pd.DataFrame(data)
print("=== 元データ ===")
print(df)
print("並べ替え")
print("\n=== PERが低い順 ===")
print(df.sort_values("PER"))
print("\n=== ROEが高い順 ===")
print(df.sort_values("ROE",ascending=False))
print("\n=== 自己資本比率が高い順 ===")
print(df.sort_values("自己資本比率",ascending=False))
print("\n=== 平均値 ===")
print("平均PER:",df["PER"].mean())
print("平均ROE:",df["ROE"].mean())
print("平均自己資本比率:",df["自己資本比率"].mean())
print("\n=== 条件に合う企業 ===")
filtered=df[
    (df["PER"]<15)&
    (df["ROE"]>10)&
    (df["自己資本比率"]>50)
]
print(filtered)