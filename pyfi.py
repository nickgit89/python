from fs.osfs import OSFS

with OSFS(".")  as myfs:
    if (not myfs.exists("cooldir")):
        myfs.makedir("cooldir")

    with myfs.open("cooldir/coolfile.txt", mode = 'w') as c:
        c.write("This is a cool file in a cool directory")

    with myfs.open("cooldir/coolfile.txt") as c:
        content = c.read()
        print(content)

