
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


posts = [
    {"title": "Python-a giriş", "author": "Aysel", "tags": ["python", "başlanğıc"]},
    {"title": "Web dizayn əsasları", "author": "Kamran", "tags": ["web", "dizayn"]},
    {"title": "Data analizi", "author": "aysel", "tags": ["data", "python"]},
]


def postlari_goster():
    if len(posts) == 0:
        print("Heç bir post yoxdur.")
        return

    sira = 1
    for post in posts:
        teqler = ", ".join(post["tags"])
        print(f"{sira}. Başlıq: {post['title']} | Müəllif: {post['author']} | Teqlər: {teqler}")
        sira = sira + 1


def yeni_post_elave_et():
    title = input("Başlığı daxil edin: ")
    author = input("Müəllifi daxil edin: ")
    teqler_str = input("Teqləri vergüllə ayıraraq daxil edin (məs: python, data): ")

    tags = [t.strip() for t in teqler_str.split(",") if t.strip()]

    yeni_post = {
        "title": title,
        "author": author,
        "tags": tags,
    }

    posts.append(yeni_post)
    print(f"'{title}' adlı post uğurla əlavə edildi.\n")


def muellife_gore_filtr():
    axtarilan = input("Müəllif adını daxil edin: ")

    neticeler = [
        post for post in posts
        if post["author"].lower() == axtarilan.lower()
    ]

    if len(neticeler) == 0:
        print(f"'{axtarilan}' adlı müəllifin postu tapılmadı.\n")
        return

    print(f"\n'{axtarilan}' müəllifinin postları:")
    for post in neticeler:
        print(f"- {post['title']}")
    print()


def butun_teqleri_goster():
    teqler = {teq for post in posts for teq in post["tags"]}

    if len(teqler) == 0:
        print("Heç bir teq tapılmadı.\n")
        return

    print("Bütün unikal teqlər:")
    for teq in sorted(teqler):
        print(f"- {teq}")
    print()


def menyu_goster():
    print("=" * 30)
    print("       POST MENYUSU")
    print("=" * 30)
    print("1. Postları göstər")
    print("2. Yeni post əlavə et")
    print("3. Müəllifə görə filtr")
    print("4. Bütün teqləri göstər")
    print("0. Çıxış")
    print("=" * 30)

while True:
        menyu_goster()
        secim = input("Seçiminizi daxil edin: ")

        if secim == "1":
            postlari_goster()
        elif secim == "2":
            yeni_post_elave_et()
        elif secim == "3":
            muellife_gore_filtr()
        elif secim == "4":
            butun_teqleri_goster()
        elif secim == "0":
            print("Proqramdan çıxılır. Sağ olun!")
            break
        else:
            print("Yanlış seçim! Zəhmət olmasa yenidən cəhd edin.\n")
