#! python3
# January ‎28, ‎2018

from tkinter import *
from tkinter import ttk
from os.path import exists


class AboutDialog(Toplevel):

    def __init__(self, master, window_title: str, about_title: str,
                 content: str, bg='lightgray', image=None):
        self.window_title = window_title
        self.about_title = about_title
        self.content = content
        self.bg = bg
        self.image = image
        if self.image:
            self.image = PhotoImage(file=image)
        Toplevel.__init__(self, master)
        self.geometry("+%d+%d" % (
            master.winfo_rootx() + 30,
            master.winfo_rooty() + 30))
        self.resizable(height=False, width=False)
        self.title(self.window_title)
        self.transient(master)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.ok)
        self.focus()
        self.master = master
        self.bind('<Return>', self.ok)
        self.bind('<Escape>', self.ok)
        self.create_widgets()

    def ok(self, *args):
        self.destroy()
        return args

    def create_widgets(self):
        frame = Frame(self, borderwidth=2, relief=SUNKEN, bg=self.bg)
        frame.grid(column=0, row=0, sticky='NEWS', pady=5, padx=5)
        # Title
        if self.image:
            Label(frame, image=self.image, bg=self.bg).grid(
                column=0, row=0, pady='5 0')
        Label(frame, text=self.about_title, bg=self.bg,
              font=('courier', 24, 'bold')).grid(
            column=0, row=1)
        ttk.Separator(frame, orient=HORIZONTAL).grid(
            column=0, row=2, sticky='WE', padx=5)
        Label(frame, text=self.content, bg=self.bg, justify='left',
              wraplength=400).grid(
            column=0, row=3, pady=5, padx=5)
        Button(self, text='Ok', command=self.ok).grid(
            column=0, row=4, sticky='WE', pady='0 5', padx=5)


if __name__ == '__main__':
    root = Tk()
    icon_bytes = b"""\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x002\x00\x00\x002\x08\x06\x00\x00\x00\x1e?\x88\xb1\x00\x00\x00\x06bKGD\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07tIME\x07\xe1\x06\t\r\x08\x1c7\x84\x9d\xb9\x00\x00\x10`IDATh\xde\xe5\x9ay\x8cd\xd7U\xc6\x7f\xe7\xbe\xb5\xaa\xba\xab\xd7\xe9\x99\x9e}\xc63\x99\xf1\x12\x1b\xc28\x0b\t(v\x9c\xc8Q\xc48\xc2\x8a\x00\x81X\x84 \x04B\x98\x08"\x04R\xd8"\xa1\x80\x84\x129\x08%BH\xa0\x00\x82 \x96,\x90\r\xb2\xe0Ibg!\xb13\xf6x6\xcf\xd2\xdd\xd3\xdd\xd5{mo\xbd\xf7\xf2\xc7{\xd5]\xbd\xd8\xb1\'\xe6/\x9et\xfbu\xbd\xaa\xf7\xde\xf9\xdew\xcew\xbe{\xab\x84\xefc;q\xfa\x0c\x17>\xf1\xc1M\xc7^\xf3\xf3\x7f*\xcd\xb5\x86\xcat&\xb9\xceE\xa1\x14\xd6\x1a\xe5\xba\xd6u];\\\xaf\x9b\xaf\xfe\xf5\xef\xd9\xefu\x9d\x17\xbb\xc9\xad\x9ct\xf2\xa1w\xa3\xb5\xe6\xd2\xa7\x1e\x01\xe0\x9e\x9f\xf8m/I\x92\x894\xc9N\x82}\x85 \'E\xd4\xa4\x88\xd4\x11\x1c\x0b9\xc64\xad\xb53\x16\x9e\x12\x91o\xfb\xae{1\x08\xc3\x85\xef|\xec\xfd\xfa\xa5\x00#/\x16\xc03\x1f\xff\x00{\xef\xfbEn~\xf1\xaf\xb8\xeb\xe1\xf7\xd4\xe38\xfeA\x9d\xe7\xaf\x11\xec+\xc3jm\xd2\x0b\xfcI\xd7\xf5G=\xd7\x1dp\x94\x12\x94`\xac\xc5\xe4\xda\xe6y\xde\xca\xb2l1M\xe2\xb98\x8a\xa6\x94\xe3|\xd5\xf3\xbcG\x07\x07\x07\xbf\xfb\xcd\xbf{_~\xe2\xf4\x19\xb9\xf0\x89\x0f\xda\xffs /\xfb\xb1wq\xf1\x93\x8f\xf4\xd2\xe1`\x9ee\xa7\x95\xe3\xbc\xc5\r\xc2\xbb\\/\xdc_\x1d\x18`x\xa8N\xa5\x12\xe28.J)D\xc0X\x8b\xd5\x1a\x9d\xe7$IL\xd4\xed\xd0\xedt\xe8\xb4\xdbW\xe28\xfe:\xf0\xd1\x81\x81\x81/?\xf1\xb1\xf7wo\x95\x99[K\xad\xb7\xfe\xc6\xa0\xce\xed\x19\xc7q\x7f\xb960\xb0\x7f\xcf\xde\xbd\x1c9p\x00\xc7\xf7i\'\x9a\xcc\x18\xac\x05c,`\x11@I1\xb0\x06\xabs\xd2$\xa617K\xa3\xd1 \x89\xe3\xcf\x18c>p\xf9\xdf?\xf4\xb9[\xad\x1b\xe7V\x80\x8c\x1d\x7f\xd5O"\xea7G\xc6w\x1d\xbc\xfd\x8e;\xb8\xef\x95w\xf3so\xfa\x01\xee9\xba\x9bK\xb3+\\\x9f_\xa3\x13%\xc4IF\x9cdDIJT\xee\xb3L\xa3\x1c\xc5\xe0@\x85\xf1\xf1q\\\xd7\xa5\xd3n\x1fK\xe28\xd9}\xe7\xeb\x9e\\\xbc\xf0\xd8\x1a\xc0\xd2\x85\xc7^TL\xee\xad\x001\xc6\xfe\xcc\xd0\xc8\xd0\xbe\xb1={\xb9\xe3\xf8!\xde|\xea\x08\x87\'\x06\x01x\xf0\x15GX\xeb\xc4\\\x9c^b \xf4\x8b\x13l\xc1\x0c\x08\xdaZZQB\'I\x19\x1f\xac2\xb9g\x92\xb5\xd5U\xe28>\x9e\xa6\xe91\xe0\xfa\xad\xc4tK@Dd<\x0c\x037\x08Br#DI\xb6\xfe^\xaeMqaW\xe19\nkm\x99\xc1\xb6\xc0\x82-\x92\xcdZ\xbaI\xc6\xe8\xa0O\xb5\x1a\xe2\xfb~5I\x92\x91[U-\x97[D"\xa2\xa8\xf8\x1eK\xcd\x88O\x7f\xebY\x9a\xdd\x8447\x9c}z\x86\x95vB5\xf0\x10\x05b\xa5\xc0a(^\xf7\xaa\xc6\x16\xe2\xa4\x94\xc2Q\x0eJ)e\xacu^R \'N\x9f\x01x\xceb\xb3\xd6j%B-\xf4q\\\x87\xab\x8d\x16\xa9\x9e!7\x86\xf9\xb5\x88Z%`\xa8\x16\xac\x93`t\x8e\xd6\x86,\xd7hcJ\x85\xb1\xb8\x8e\xc2U\x0eJ\xa4\x80f\xad}\xc9\x80lU\x8b\x13\xa7\xcf\x0c\x88H\xb5|\xa9\x01e\x8c\xf1\x8c5h\x9d\xe1\xa0\x11\xab\xb9zs\x11\x04\x02\xd7!\x08\xa4\xaf6\x04\'\xf0\xd1\xc6\xd2\x8aR\x924G\xc4"Vp\x1d\x85\xa3\x04\xc4bJu{I\x80\xf4\x838q\xfaL\xd5\x18\xb3\xd7\x18\xf3j\xe0`Y\xad\x1aP \xe3\xddN\x87\x99\xe9i\x9a\xab\xab\x18\xadw\x10r\x8b5\x16D8x`?A\x10\x12\xa7\x9a\xdc\xd1(\x11\xb0\x82\xab\xd8`J[,\xaey!A\x7f\xfe\xcf\xe1\x8d\xef|\x1e } B\xe0g\x95R\xef\xb3\xd6\x8e\xef\xc4x\xb3\xd9\xa2\xd9j=o32\xc6 "\x8c\x8d\x0e\x13\x84!\xae#\xb8J\x10\x11\xc4B\x92\xe5t\xa2\x94(\xce\x11\x11\x1ce\xd5\x0b\x01\xb2\x15\xc4\xa6\x18zl\x9c|\xe8\xdd\xc3\xd6\xda\x9f\xb6\xd6\xfe\xe1\xd8\xd8\xe8\xd8\xd1\xa3G\x19\x19\x1d\xddH\x95\x1e(\xbb\xfe\x07\xa48n{\xeaT\xd4\x11\xd6Z\x04\xcb\xe8\xc80\xa2\\\xd6\xba\tQ\x92\x91\xa69\x8b\xcd\x0e\xed(eb(dff\t\xbf\xf3d\xebu\xbb\xcf^\xbf\xef\xf0S\x8d\\o\x8a\xcf\x00\xf3\xc0Y\xc7\xe5\x1f\x1e\xf85V\nV\x847\xbe\xd3ng\xa4\xc7F\x96e/s]\xf7\xd7\x87\x87\x87\xc7\xee\xbd\xf7^F\xc6F\x01)\xd2\xa4\xef\xea\x8e\xb0n?rc\xb0\xda`(\x82\xef\xe13X0\x96$7\xc4Y\xccr+b\xb5\x15\xd1\x89S\xe2,\xc7\x11)\xc4\xc0:x*\x1f\xa8\xf9\xf1\x1d\xca\xf5n\x1f\xddu\x04\x11\x05"Xkm\x9ev\x92\xb8\xb3\xf8\xda$\x8e\xde\xfc\xb9\x0f\xf1G~X\xf9\xce\xeb\x7f)\xca\xfb\xc1\xb8\xfdl\xdc\xf9\xe3\xbf5\xd1\xedFo@8q\xe7\x9d\xb7\xb3gr\x0fIn\xe9\xc61X\xca\xb4\x80,3\xa4yN\x9ak\xd2\\\x979n\xd0\xc6\xac\x03\xb1\xd8\xc2,j\x8b\xd6\xc5g\xa3$#N3\xf2\xbc\xa8)\xd7s\x912)\x04+\xd6j\xf1\x82\x01\x8e\xbc\xfc!\xc4\xf1\xd7\xc5"K#\xb7\xb9x\xb16s\xf9\x8b\x87\xf2\xa4\x1b%\xdd\xe8\xbd\xc0\xc5m\x8c\xf4\xd8H\x92\xe4\xa4\xeb:\x0f\x0c\r\xd69~\xec6\xb46t\xa3\x84\\\x1bD N4q\x9a\xd1\x8e2:IJ\x94\x14\x01jc1\xa6\x00R\xa0\xb0e3/\x8e[k\xca\x98,J\xa40\x93%m\x82E\xa4 \xd1\x1a\x8b\xe3\x06\x8c\xed;E\xa1\x04\xad\xe2zRax\xd7q\xac1\xdc8\xff\xd9\xb7\x19\xa3\xbf\xf4\x85\x8f8s\xf7\xbf]7{\x85\xbf^\\k\xd6\x92$\xc9\xb1 \xf0O\x1e>|\x900\xf0\xc9\xb4A\x10\\\xa5\xc82Cc-\xe2\xd9\xf9&\xd7\x17Z\xcc\xafF\xacu\x13\xbaIF\x92\xe6d\xb9)\x180\x16m\xc1\xae7<\xc1qT\xd93Ta\x1c\xcbJR\xe5\xdd\x8d\xb5\x05,)\xc0\xeb,\x83d\x05\xa2\xab\xd0y\x1a\xa2k\x04\xd5:G\xee~\x1b~eTD\xf1\x96<\xd5\xb7\xf7\x17\xfe:\x90\x1f~\xf8=\xfb\xb56\'\x02?\x18=r\xf8\xe0\xa6\\\x9f_\xebrnj\x89\xab\x8d&\xed8C\x9b\xde\xd3\x14\x94(\xcai\x07R4\xfd\xa2\xc1\xc9sw\x05k\x8bsk\x81\x87\x05\xb24C\xe9\x98\xd0\xd58^\x80r+=\xa8 \x0e\x98\x08\xb2E\xdc`\x98\x89\x83\xa7\xf0\x83\xc1;\xd2\x88\x03\xfd\xd7\\\x07\x92$\xc9\x98\xe7y\xfb\xab\xd5J8:<\x8c\xb5\xd0IR\x9e\x99Y\xe6\xd2\xec*\x9d8{\xde\x86%R\x80(F\xf9Z\x81\xf4\xe4Vm\x80s\x1d\xa1^\x0b\xa8\xd7B\xa2nD\xda]\xa6\xee\xcc19\x9cQ\x1f\xbb\rQ!\xd8\xbc\xcc\xfcJa\xd2M\x02\x08\xa3\x93\xf7\xe0\xb8\x83#Fs\xecK\x7f\xc9\xf06\xd5\xcar]\xf7|o\xa4V\xadP\rCn,\xb79wc\x85\xd5v\x8c\xb1f\x1b\x08k\x8b\xf9E\xe09TC\x9f\xd0s\x11L\x91\xf3\xf4Kt\xef\x1f\xdb\xe7\x82-XM\xb7\xd3\xe6\xda\xb5YF\xd45{\xfb\xd8e90\xee\xb2\xeb\xd0\x1b\x8a\xcf\x99\xa4\x00 .XS\xf0o5\xb5\xe1\xc3\xb8~0(\x0e\xfb\xb2\x941`u\x13\x10ct\xe8{\x95\xd0q=\x16Z1\x97o\xae\xb2\xd2\x8e1\xc6\x166b\xddr\x14\xf9\xef\xbb\x0e\x83U\x9f\xd0s\xb0:!mw\x88\xe2\xa2\xf07\xf5\x98\xcd\x88\x90R\xcd\xe2$\xa3\xbb\xb6J\xdd>\xcb\xabv\x7fM~\xe8P\x9b\xbd\x87\x7f\x94\xa1]w\x17En\x01\xf1\xca\xf42E\xa86\xc7\xaf\xee\xc6\x0bj\x8e\xe3\xb2K\xe7\x0cmcD\x81\xa3DT\x9ci\xa6\x17\xdb,\xb5\x92bf\xd7\x03\xb1\xde\xe8\n\x16\xea\xb5\x80\x8a\x0bq\xa7\xcd\xd2\xd2\n\xdd\xe6\n\x15\xb5j\\\xc9\x04ke\xb3Y\xe9Cb\xc5\x82\x91\xd0\xc62\xee\xccr\xd7\xae\x0b\xbc\xfaP\x83\xdbO\x9eb\xe2\xc8\x838^\x00\xc9\\\t\xc2[\x17\x80b\x0e\xa8p\x1c\x1f\xd7\x0bq]\xeayNm\x1b\x10\xd7Qy\xae\xb5\xee\xc6)\xad8\xc3s\x1d\xd2\\\xb3\xd5\x9e(\x11\x86j\x01\xb5@\xb1\xba\xb8H\xe3\xe64\xa6;\xc7Dp\xd3\x1e\x1b\x9a\xd25?r\x8a{o<\x80\x1e\x10A\xacAp\xc4\xd8\xa10V\x87\x86Wd\xef\x88e\xdf\xd1\xd72y\xfc\xad\x0c\x8c\x1d\x87l\xb6\x94\\\x7f\xa3\xfd\ne\xd1\xc7`\x13\\Wp\x1c\'\xc82\x1dngD9\x91\xd1y\x94\xeb\x1c\xa5\ng\xda\xe78\n\xa5\x11\xa8\x06.\xb5\xd0cm\xa9\xc1\xf4\x8d)j\xd9\x15\x1e\xb8\xedI\xee;\xf4\xa4X\xab<\xa5\xd4N\xe6K\xe8\x87\x85\xe0y!\x03\xc3\x87\xd8w\xf2m\x8c\x1fx-\xae\xe7C:_\xd4\x86\x04;\x18\xb7\x18\xd2g\x11UG\x89\x05\xe5\xba\xd6jw\xbbiT\xaac\x8cn\xea,Cg\x19\xbe\xab\x8a\x8c\xb6E\xc3\x02\x8bB\x18\x1d\x081Y\xca\xd4\xf5Y\xc69\xcf\x9b\x8e\x7f\x9d\xd7\x1c\x9ab\xd7\xe1\x07\xd9{\xfc-\x84\xb5]\x08\nk\xcd\xb6\xfa\xd8x\xc2\n\xc7\xab\xe0\x86c(@l\x1b\xb2\x06\xd8\x14$\xdc8OT\x01 \xb9\x0c\xd19\x90\x10[y9\xc6h\xb0Z\x8b\x90o\x03\xe28\xeeZ\x92%\x8d<K\xf3<M\\?\xa8\xa2\xa4\xf0\xed\x16\x8b\x88\x10\xfa.\x9e+\xdc\x9c\x99\xa3jf\xed=\xe3\xdf\x91SG:\x1c\xbb\xe7\x17\x988\xf1S\xf8\x9e\xbf\xd1?l\x9f.\xf7\xfa\x815\xa5\xac\xe6`5\xd8&\xe8N\x992\xba\xf4\x87\x1at\x0c\xa6U\xa4Y:\x03\xf9|\xf1\x9e\x7f\x0c\xac!O\xbb\xe4Y\xdeU\x8ah{\x8d\xf8^#\x8e\xec\x94\xce\xf3v\xd4i\r\x0f\xd7\x06p\x95\x90S\xd8\r\xd7\x11B\xbf\x98\x896W\x96\xd8\xe5\xcdrl|\xd5\x1e:pD\xc6\x8f>DP\x1d\x81t\x19LVf\x92[\x14\xac\xc9\xc1\xac\x81n\x16\xc3\xb4\xc0t\x8a`mR\x02\xebIs^\xb0b\x92\xa2\t\x9a\x0e\xd8\xa8\x00\xaa\x06\xc0\x19&O:\xa4I\x97<g\xc5\xf5hn\x03r\xee\x9f\xfe\xa4s\xf4\xc1w\\\xd7y\xbe\xb0\xb6\xd4\x18\x1e\xdb\xb3\x8fj\xe0\x91\xe6\x9a$\xd3\xa5\xbd\x10\x8c\xb1di\xc4@\xb8\xcah=\xa4>z\x9cp\xe0@\t\xa2O\xfbM\x0c\xf9\x14d\xf3\x90\xcfA\xbe\x08z\xad\x08\xd0\xa6\x05`)\x17&l\xe1\x95\x8b~\x91\x97\xa0Lq\x1dq\x8a\x07\xa2\x02p\x06i/\xdf M\xa2\xd8hn\xb8\x15\x1a\x9b:{o\x8e\xeez\xfe\x15\xad\xb3\'Z+\x0b\xc4\xdd6\x03\x95\x80Z% \xf0\x1c\\\xc7\xc1Q\x1b\xb9\xefH&\x9e_\x137\x18)\x15J\x81\x1a\x04U\x05\xdd\x85\xf8\x02\xb4\xbe\x0c\xcd\xff\x82\xf6\xe3\xd0\xfd.\xc4W!m@\xde,\x80\xea\xa4L\xa3\xb8d\xd2\x94i\xe8\x96\x05\xef\x801`\x15\xb8#\xe0\x04,\xcc=C\x9ev\x17D\xb8t\xff;\x98\xdb\x04\xa4\xe7~\x1d\xc7\xbd\x08\xfcG\x9e\xa7\xc9\xec\xb5K\x88\xc9\x18\xafW\x98\x1c\xa916\x18\xae\xa7\xd6F\xaf\x16,N\xa9\xf7a\x11@:\x03k\x9f\x84\xe5\x7f\x84\xee\xb7!o\x14,\xe0\x14\x92*\xeezO\xd8<d\xbd\xe9\x17\x13\xb8\x92!\x9b\x82\n\xc1\xddC\x9e\'4\xa6\x9f"K\xbb\x17\xfc\x90\x8b"\xc5\xb4w\x93\xd7\x028\xffo\x7f\xd6Q\xca9\x8b\xe5s\xcb\xf33\xdc\xb8x\x8e\xce\xea"\x9e\x18|e\xc1hL\x96\x83\xe9\x9b)"\xa0\xfc\x82\xfa\xf6YX\xf80\xb4\xbe\x02&-\x00\x12\x00%\x00\xe5\xf6\xa5K\xdfPN\x1f@\xd9Pk\xabA\xaa\x10\xec\'\x97!n>\xfb\r\xd2$\xd6\xc6\xf0i\xe5pq\xc79{orU\x1f\xd9}\xa9\xb92\xffnkm\xbc\xb68w_s\xb91\xa4\n\xbf-={\x92\xe7\xd6\xaa\x01\xa5D\x94BBAwa\xe5\xef\xa1\xf9\xa5\xb2@\r\xb8\xc3P\xb9\x13\xdc\xfaz:\xca\x0eb\xbc\xdd\x1a\xcb\xc6\xf4\x19ADa-4\x97\xa6\xb8~\xe9Q\xac\xcd\x9eQ\x0e\xff\xfd\xc0\xaf\xb2\xd8o\xe37MuO\x9c>\xc37\xfe\xe6w\x00\xae\x9c8}\xe6\x0f\xf2,\xfd\x17\xad\xf5mX[_\xcf(\x01\xd7\xab\xb2\xbb\xbapW\xd5\xcb\xefM\xe3\xc5\t:\x8f\x17,\xe4\xcdRf\x8b\x1e`\xc5\'\xea\xc6\xdc\x9cz\x02\xac-\xa5Y\xb6\xb7J\x0b"\n\xe5\xb8\x88R\x18\xa3\xd7\xe7\x8d`I\xa2U\xd6\x96\xae\x11uZW\x95\xe2\x8f\x1dG\xce\x83\xdd\xb4\x9a\xb2m\x15\xa5\xc7\xcc\x85O|\xf0\xe9\xfb\x7f\xe5#\xe7g\xe7/\x8d\x83\xad\xf5V:A\x98nMd\xf7\xec\xba\xfc\xf0\xa0;r8\x8bg\'$\xb9T\x18=q\xcbg\xbe\x91\xdfY\x12\xb1\xbap\t\xacA\xf5fR\xebKt=\x07"h\x9d\x93\xa71\xda\xe4\xb1\x88s\xa5\x84\xab\xac\xb56K\xbbq\x1cu\xa7\x1c\xc5\xe7\xad\xe5\xe3o|\xa7\xedl]M\xd9\xb6@\xd7\x03\x03\xf0\x85\x0f\xbf\xdd\x02\x0b\xe5\xd8\xb4\x1dx\x90\x05\x97nj\xf2\xd6F=\xd8\xa8\xec\t=)U\xf8\xc1\x00\xbb\xf6\x9c,,\xbe\xc8fg\xdfS\x1c\xc7\xa5\xd3j\xb08w\x89\xd6\xda\xea\xa2\xc9y\xa4\x940\x070\xa2X\xf5|\xae\xf8>O\xbe\xfe\xedE7\xdf\xba\xb6\xb5\xe3\x92\xe9\x0eK\xa5\xbd\x9cP\xbd\n\x9e^b\xf4h]|\x11U\xe6u/\xf8R\x08L\x86\xe8\x88JP\xe7\xd0\xe1\xbb\xca\x0e\xcf\xe6e\xa5\xde\xb1`\x90\xe6\xc2\r\xa2\xce*\xed\xd6\xea\xea\xc3\xef\xe5o\xa3\x98\xe4G^\x85}\xe01\xcc\xefo\xc9\xc6\xcf<\xf2=\x16\xe8\x9ecS\x85\xecP\x01\xaa\xe5>\x9c[a\xf4\xe0A\xe39b\xcb\xac\xb3\x1b@P\x90/A\xfb\xb1\xad\xc2\xd8\xf7hT!\xc7&\x85\xfa\xddX\x93\x17+&\x1a7N\xd8\x0bt\x1e}\x9c\xf8Q!\x02\xd2\x92\xa1\xe2\xab\x8bw\xbd\xb8\xd5x)\xb5\xb3\x02\xd4\xcaQ-\xf7a\xb3\xcd\xb0\xd6\xe2Io\xbe`z\x8c\xb0!\x9dt7l8\x80\xcd\x8a\xe0\x87^\x0f\xfb~\xb7\xe8=\x0b\x1f\x05}\x15\xec\x1c"\x82\xd6\xf8\xc0\x1e\xa0\x05\xc4@\xa7\x1c\x11\x90<\x97\xf0\xb9\xcf\xc3BX\x06=\xd07\xd6\x015\xdb\xd4\xb2,w\xb0Y\xb1\x98\xa6\x06![\xeb\xb3\x16=&L9\xdb\x93\xa2\xe3W\xf6\xc3\xe0\x8f\x82\x7f\xb0x{\xf44\xb4>\x05v\x06cr\xb4F\xace\xa4\xcc\x82\xa8\xdc{e\xac\xaa\x04g^\x08\x10)O\xac\xee\x00\xa4\x07\xa6:\xbb\x0ck\xcd\xae\xee\xb6\x16H\x92.\xe1\xc0\xc9\xe2ae+E/1q\xc9\x84\xda\x90\\\x93\x16\x12\x9d\xcc@\xbeRtl\xc7@n\x88:\xabt\xda\xcb\xe9\xec\x127\x81\xc1\xb2\xd0\x1d\xfa\xfa}\xdfBz\xba\x95\x19\xe7y\xd8\xa8\xec0\xaa\xbd:\xd1\x86\xe0\xe8${\xc6\x87\xd2\xbd\x9e\xa7\xf0\xab\x93x\xe1(\xf8up\x82\xd2\x8e\xf8\x85\xe1\x13\xaf\xf0NN\xbdp\x00\xae\x07\xfe\x10\xe4\x8b\xa4\xcb_ay\xfa\xab4f\xceqm\xbaq\xf3\xb3\x8f\xf3\xe8\xb9+4\xca\x80{#\xef\x1b\xbd\xd7\xf6\x85\xa4V\xff\x130\xe5\xe8\xff\x9fKS,}\xed)\xce\x8f\r7G\xb4~\xfch\xb7\xd3\x94}\x07\xee\xc6\xafM\xe0\x04{P~\x8a\xb2Q\xe9v\xcb\xaf\xabT\x05+\x01\xdax\xe8\xc6g\xd0q\x87\xc6\xcd\xa7\x98\x9b}\x9a\xe9\xd9\xd5\x85\xff9\xcf\x13\xff\xfaE.\xecp\xff\xad\xac\xbc\xe0oum\x1f\xb5jg\x87\x87\xbax\x83\xe5\xa5&k{\xc7\xf5\xa0\xcf\xdc\xe8\xcd\xe9\xa7Y[\xba!I\xdc\x05\xf1q\xfd\x11T0\x81uG\xc0\x19&\xcb\x1dZ\xadU\x1a\xb3\x17\xb9~\xf9k\\\xbdt\xd6.-^\x97\xe9\xb9x\xea?\xbf\xce\x17\xfe\xe2\x9f9\x9be\xb4\xca\xda\xe8n\x19qy<\xda\xa9F\xe4y\x14k\xa7:\xe9W\xae*PQB\xb0\x7f\x82\xfa\xab_\xce\x89\xfbOqjr\x97\xda_\xf1\x9d\xaaRJ\x81BDD\xf5\xdc\xb8\xb1`\x8d5\xd6\xe8$\xd5\xd1\xe2\x9a\x99\xfd\xe6y\xbe\xf5\xe8\xb7\xf9\xee\xf9k,d9q_\xe0\x9d\xbe\xd1.\xf7] \xdb\x89\x15\xf9\x1e\xf2\xabJ\t\xae\xf6\x8dZ_\xcd\x84={[\xafQ\xbb\xe3\x08C\xf5\x01F\xf7\x8e1>9\xc6\xd8\xd0 \xf5j@\xd5uq\xb5&\x8f\x12\xbakm\xd6\xe6\x97Y\x9aY\xa0\xd1\x8dY\xba8\xc5\xea\xec\xe2\xba\xd4\xa6}O\xbd\xb3\x85\x91\xa4/\xcdn\xe9\x97\x0f\xe5\xbcu\xdd\x93\x87\xfd{\x11Bk\t\xfa\xd24p\x1d\xaa\xc7\x0eP\xdb3FX\xaf\xe2\xba.N\xae\xd1\xed.\xd9\xfc2\xd1\x95i\xdaq\xba\xde\x1b\x0c`DH\xac%.\x01%}\xfbl\xa7\xe2\xfe~\x7f\xc2\xa1\xca\x80\xbd>p[\xc7V\x8bkwXN\xe9\x97\xd2l\xcb\xc8\xcb\xbd\xde\xa9\x16^\xd2\xdf\xa2\xec\x90~\xd2\x07R\xb6\x88B\xff=\xcc\x16\x15\xd4[\x14\xd1\xf2\xff}\xfb_\xf9Q\xbf\xe0\xcfX\x02;\x00\x00\x00\x00IEND\xaeB`\x82"""
    if not exists('py.png'):
        with open('py.png', 'wb') as py_icon:
            py_icon.write(icon_bytes)
    AboutDialog(root, window_title="Window Title",
                about_title="About Title",
                content="This about_dialog.py is written by "
                        "Denniel Luis Saway Sadian. The appearance "
                        "is copied from the IDLE's about dialog.",
                image='py.png').mainloop()
    root.mainloop()