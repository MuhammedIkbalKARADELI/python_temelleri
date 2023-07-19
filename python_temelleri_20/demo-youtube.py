import pandas as pd
from pandas.core.arrays import categorical

df = pd.read_csv("GBvideos.csv")
print(df)


# 1- İlk 10 kaydı getiriniz.

result1 = df.head(10)
print(result1)

# 2- İkinci 5 kaydı getiriniz.
result2 = df[5:].head()
print(result2)


# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result3 = df.columns
print(result3)

result3_1 = len(df.columns)
print(result3_1)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)

df = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1)
print(df)

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.

result5 = df[["likes","dislikes"]].mean()
print(result5)


# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.

result6 = df[["likes","dislikes"]].head(50)
print(result6)

# 7- En çok görüntülenen video hangisidir ?

result7 = df[df["views"] == df["views"].max()][["title","views"]]
print(result7)


result7 = df[df["views"] == df["views"].max()]["title"].iloc[0]
print(result7)


# 8- En düşük görüntülenen video hangisidir?

result8 = df[df["views"] == df["views"].min()][["title","views"]]
print(result8)

result8 = df[df["views"] == df["views"].min()]["title"].iloc[0]
print(result8)

# 9- En fazla görüntülenen ilk 10 video hangisidir ?

result9 = df.sort_values("views", ascending = False).head(10)[["title","views"]]  # azalan izlenmeye göre sıralar.
print(result9)


# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.

result10 = df.groupby("category_id").mean().sort_values("likes")["likes"]
print(result10)


# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.

count_categori = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]
print(count_categori)

# 12- Her kategoride kaç video vardır ?

result = df["category_id"].value_counts().sort_values(ascending = False)
print(result)

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.

df["len_title"] = df["title"].apply(len)
print(df)

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split("|")))
# print(df)

def tagCount(tag):
    return len(tag.split("|"))
df["tag_count"] = df["tags"].apply(tagCount)

print(df)


# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

def likedislikeoranhesapla(dataset):
    likesList = list(df["likes"])  # listeye çevirdik
    dislikesList = list(df["dislikes"])
    
    liste = list(zip(likesList,dislikesList)) #(26126, 599), (75335, 2106) birleştirme yapar.

    oranListesi = []

    for like , dislike in liste:
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))
    
    return oranListesi
    


df["popularity"] = likedislikeoranhesapla(df)
df = df.sort_values("popularity", ascending=False)

print(df.head(10))

