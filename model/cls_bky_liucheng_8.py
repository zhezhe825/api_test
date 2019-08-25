import requests
import urllib3
urllib3.disable_warnings()
import re

class BkyLiuCheng():        # class类，以前都是封装在函数里面。现将“博客园的登录流程”写成class类
    def __init__(self,s):   # 初始化，就是把后面用到的公共的参数提取出来
        self.s = s

    def bky_login(self):
        """博客园登录"""
        s.verify=False
        url = "https://www.cnblogs.com/"

        c = requests.cookies.RequestsCookieJar()
        c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8D8Q4oM3DPZMgpKI1MnYlrntZQZgzcYrfe4AefenTz3QdPCNxa7wT6Ws7f4gVEzoA1bjO_py-JV8cicE929WESLe1KdozvNrmyhfC53b1HJ53Ys5hpU2UiGi2KpwmFS5m-KRzRYYVMJPWZiGYKWoh7sBcG7OG9IRerp6DGEL6tMO7xaHG895ag26BAgpbQMh3_pH1so7AuIqUvWtdj3_gZ8K177pF6Gk4h2iHVRzQpIkDflhdITSqpq8Vcsilh_38VaQg4Rz2rjPbOwHSupWbGmlortv_G0ElxOLCcLzVeWcm7ARRwCIXVQ7FEbYTEp0LEfvK5RsVDt-FFWqLYtrsajpumCZf2pDHJwDWIkibmkDFAO1MrY2XBNPjgHgMOeZXdv0M7-72myesmZtI37eaun-W3FuQ39cLaO3lRkzZU_mPeLn2WVGXWV72hdI7Gdq-nWZ4XqlaBtsr6ovB865M2o")
        c.set(".CNBlogsCookie","1C471FCB3DBD9760AF2B961873F3DA2F1185FA4F30601E92CDFF1B31B750B818AF4577342983A15C90B02834594E5AD1431AC3845BDF7697AD5938BF48292E6283772F1076052113E1F38B35A7A387F939C4346A917245B4BE70BE31CB11007761D72E93")
        s.cookies.update(c)

        r = s.get(url)

        if "开发者的网上家园" in r.text:
            print("博客园登录成功！")
        else:
            print("博客园登录失败！")
        return s

    def bky_save(self):
        """博客园——保存随笔"""

        url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
        body = {
            "__VIEWSTATE":"laiLJPulLnOF8imnA4zrZ2UtqnWHFpov3pK58D4spGy1amzgWCFBly4fFYH8ZpiBo25KfxAAzc6SvWTq3oJJhc8YUv+5tGCXWw5gwvvLOOLf3bHrTTB8xlzmsu1wVFyWd/HmffTkbc4zFRRWABh+zcMOGSE5egewdm7LhQHXALbvQuq10gVhLwyb5eeDwymfaJZW7R4loGAOEGJIYGzISr6yhjeC15Duoiq4X8lP+f2F50qOH4af4cpv1gQLOfjTkl7PZkPkeXUsbqF2Zlc23FD76CcfKSmq1DsUQNsFaNAdcjv3UoDLKTNli3CS/E4wuu9dkcfmDZQqdgXkqnRCHZOU10j/xSL1a0tc8lT0rLVRScJLzj5hexmMmbO84JhiijfkJq6dR7yy6fK/h4rCoriyRxhdJ4/u/BZKs5YE7JR+FJjqc2sAFNMS725T9W8rrYYqCXJkNUy+CBYoXvrtOImS/UjRh8aPtsL+35H78RgtviuoqolRTw7h1pm5p2tusKt1F+ILIMlD+JtQofjYuzD01rp89F09NdMwqosBGkP8pOP81bqZBA8fqf7z9mf4Te4a0hC6Wiamss8nnA69MHTAoVpxBWfSeN7l0w3MmiOluK+1C34Oz6TgLd0lKRVf8fI4MEr87jPDcJ8/IiwjtX15WFkblctJT+wE82Evd+QCc7Gu5STP+hRSn9vs80qo4WyVRE5VHAaA1H3qsNtbsJYH3lgcULjj+LvcRooIx2iXM+W6nvd+mwjIGh2pNYV48fSoR8zn/1PAcF05naFwFOYlvuXHZju9P/wwuE0ydJaKXpJoRcedPEri/lAO03pwhhq1I9Mhr2AGptHXYzaTtBgvG2opfvJlMd4uI1EriXrhwb8LQX5eoQOkC04BVowgNUOJu7Jk1ZwLckRSJdFP1qgaIhKKoqw256gEueaKDpZBrPKS7YSXGaW2u6yCz6gwC58Bhddk70SOT8TssIvA7GbjNeTkZtyX9nU7c6YbP7dS25B7LyMz4FKxBnKdGUbbRTubTbHjtJEexRoOUwcTSJI07mzJvANOs4FfQsAElT727ZiYQty8lgsazHik4W46ccRhIiu75ZwukEzSusg+EKlsMjTdeQS6s23bFP0kl5OAUPLTL9vq+s0R0jpZAWg4mgkeNvgwy7Dgc+3cibIxIc5XhkKkzcDNb0OpmoKnOp4X4urUNQfIZtBgcGYIBAHPYpiuk3oH4Km0XCnGikPlFLTa3oCOMlViY4IqlWMyVZHkZEvlXTmfxh9TS6y+8iK0SlqZ/pzoBn88u3W6jGGUgkK0GRu5GKjszAz3zXgt5B3wuPXeTcp8WbhXNTle3BDxJ9sAQtQOwC4u3KBttYPoS2AgjuFI8vxt0x1N1Ut/hiKanAkOAz8zbENgs+vDW8len4DLJBTaqXkFqj/r9yrj3rrDkB8VtG5xHYxa6I0f0ZymoxWPPH4k8Kd2Y8IrMMP35zhO/AwP6NRWRqJadCsD3/f26ufcV5uNS+gPj81gN2clgrYeTvv/OSJPbqZTkI6VDf3wmuZ1jk1jIcvtHBY7fDgwEx9hYh8cgq8iNpszusf7MhD7P0qm1huiUfWrVNGaZb96q1yyIdbJt42+l7XgIhxxiUbaqLKQyMnPWKJNmOhkwYXhOAmMo8yn5MG88L/VsttRbdabqtkMtEYac2x/TxIS94WWmmS3wtQK2zrVcL2cYYcpHHX6e/7diEkBgtClRnsuT2VBisJiOOYlTwmQ+FQTpH62Y4qs88lh11VWX0203pJxBjHghht246Uuj6aBO9qx8/2SPtAjyOKWK7BkXydzH0bzZVHsBkUN4DXR+XNifZ6lUfjTNLJOHUZP6WKXEWVWLC/gqJKSw/NQyd34Dj9I0f4eD0OhXq7KCPFXQ09AWM/MnAaUqvl1viH0VmdusoAluxkuHZNKamXJA9/UfI/oNT1YFv5n3PbfkmxcJT2VNDklJKSOY6DPu1lf4IcVDQ1GLLs5ozSQ13pI3SZGHuyBxUDwSU9WEobJapN0zlZ0W4//2fSN5ZfADRUy8KNfhvXhW1KupwSJd1Otui6+2z3D+9OitSllMe1hVMsl90DfNtVhAEfMNBCxlzCbkuo7r1sbtwH+8NatRxIo5wMRMpMKAribm/CNbn51xf5ge8WbrpzvZCBeZD4sEf6sE1UfRy7tvCgpOck6Ug6GeQ8hdcLKVGfC3Ej7rcsQ7tqkKJgoBZrwDEePvPcnTU56405treQP3XMefucYMDEQf2n5BMOzkwIvdgId/Ztqw+19VHlwnyBeru1Axp0mwRG0yO/dlDKoja+ECOGRCFJuNHoRptZhJVK1jLDMPVfiRol++oPy1WCeQHkxN5s2PiP7coIwEg8yAlBizU4Uf5hNnkxanhKyMIYYx4Ikvm3be/RduZqkMyv/yFhhtAFO2YSYMXP/D3wF87/N0oehUIvO/j8i/dpGtWhcADFtbWYi8oGCmR/k2Ez0ucrX/JkkAlfro8vORVhaSm4fauZ2c8zNq3sdRyrBc6FzD69yBJjPlrK9tmh+DEshXJlaEQcZV05sBETDXdHki2hI5tM1kMscs/InglT34q7FtSnJP/yX+k1dquzSCup1i97s/2aOO3RJ/xrG8F2gzuTzW/coFCy5L865Hb4UqNwkPPv9ZvGpwI5Lnl/tuFIuPkuarkgYeST/hxMLhpr36ZiAy4Xl3T3M0LABgpQDne2b2fzKM9HI+F3IzUnS02cxI+JC62jmY6h5EGEoVaii65nXXotYpN8WuorXLbAcrLTYYME1u5hcWeDDRdTHu4Gu0tRI7MS94cZDdRLzoQYWrzexMZi27v9bQMm+tHAqvVQBieOYwhi9kMAunV4fKwrQ4Jq0xl4/H7pmc/PdHC8G7nKRIl0trPMMkj2I+g+DRDvP18V1EtX3ATy4qEJwmESPoBjAbyEStia4/HN4rcrQVnpSHdR1FWR9LKHo1p0q1jchVLHtGZgGjAG7hz+NQ5q7zJs8iuDOUHJ+wHRnCmU13kyvFyzArD9m0vsifmUvxt57XlyF8Ldkt58Yyg4KzcQlvJSGrbjiB9vGOebAQBWNjH3HKstxNhd+tah+mnCK3ylGkSeY6M6j6XBCwLEKo5s277ZEyKhstBnAmLWcs8dlpuuvc3v08nwlPvEem0EIkj/G/eZHBRWkZJ83hE/5jKLTvoRjOMKpwEDYx4t4GTRNYMIsMKma7G/COwvNFYM7D9rSeqdFP9C0hRL+2kZ21t7FF5h/ZAMX3PX453lWY4vbt12ZZ5Ta0KtPOF9tLEwBMo6I7ceORTrytjROMcCmBv2l1YYPexogGK/i8JR46g9EV8ueHdvk9Aqu7KsXNtVnD0u5J2BEiAEfhGqzx9c05MWXyX1mkVpzvXjDnxCPufq1DxNQWS1VjK4hQ8yqy8qVTFSdm4FxUeDRUA+WfvSHn/cHaEwmItG5wrgn50Yh180E5IIFNjkPAMQKzBj6yU8Xe+50iSgZzJu8476WwWeXAKQsfKjjzuj6HKzSKM+nIHIVuWAHoh0+rY/V+pnvLte1+21j/bz2Lpil5QWFf6oLPAr/mFqS+Hr97wW0EYUFonWx+HMzX+a+FlCTmfyCv+HliTlo2V0jMNHLnFxW2tyO3HJHm9FG9m+aOKHZnm39luMnSgQqUI+CEmMf+1joI6RcV/UM0j9wY87IBlofckZGF67z8+/hLmF2zdXtK0MjyuepaQJ2a7ExW09ewhi1XQga3tOF6HZ69xbctxqi8y61J6jcCSfJ0MfOavnrffz7jq83os2YH79HiGGqMyi4ju3SSH64zFF+NJ4C4jgvMQgVoDosx9/VFIUK0mEljM7gC1l1eDw+MygBks8uRafhv2IJW7Qn6QYVPPiaJjbHMk9M1+XVNIFOAfz0OCc41k7tBe//fh6y/QhWVVHQZeLdc4Xfba6o9+cRepdLvMM970I1MlQSCOTk1BHKtSImezrkdKwECKGK9X7caU9LCc+KnLNXhdSAgr1ftDJUyDyaXucEagq5B1wnogna4WXPPB/g928+TlxvxurJaDhvlhBJwhebGdpu9adbGVlFFSvwmrN+sPX7eRBGEskkoasDuP0A8vBQQI/hh2Ws4YWplLhdtvqxg5YG5/HjxfzV6STjot7dPuSvBLqpHNM+cZTUI3frJzDRdfQ++wXuf0gXUV6e0adK2bHpDwk0kT88iaJ/fsAiHiYK0q+Dmfo7oF6iTFBDjmFO6MFaTG/EHjBe1cGi12F/2BixA4lAtpwz+0Eja976kD2ROKEN2igz6BRyJJ9Avv0CcB/QnsXb4qn+uemdHUp4KMEWpXM6Q2C+v1DtRKibQ4nPT0REl5+ekYECd7e0xA5e+W9lVAe4/FBFKCQ4fNJytZ/lvC6XRfsUhQl8PtXuVwNl30hacEnBWii3GlDHJOTY/USx36u6S2UfI78pDsopkVU9T2/mbRYAmQuTfm7YlYJXgzTa7sPxsDglxQoedf17qKPlKLa/YdQrJ0NUYZWkgsovWilaAdfokICZXhci6ZDG0zIG7Cj1yhpdGPe1Fn7Ic+8hECnMRPLPv9bUPfGtSINHqMtZw8UcEvFkR73B4nlXbxisWJ6PuNzvFp3D5xbXEzm1iLFeHDbPKjZkvm4GD3y35AF2/pis9HBAbslteFvRkGv/+I/ht0fKGNrG4qmf/au5cSkLItSdxWivosSfHWPA8V2Yv4GCXpMReD/yFZLb/IlHvkh3UNFpCevyTUuoAg/OJggPG93vTZ5Hk5rkuyQd0AF0ryixGY5LePl5ky56YhjBemOopJ2g6QSX/EMoVjxWQcUDM/4gcbD2+FZjHOQtb4ruFH4V4ynIpb501biddKa89D28VgAXFM1GzwweO+U3Np1nac5G/VWwZ5iyyNreEmnDymi5g43g+BkEEuLqm+Llg/1P08t3lNG5swfy9EkR27AwBOmfmjbTbd78NOYDINmnaL3hhChPJjC7nVbYT/jUdFxJTMM/E9X61487RHELRiapHJMn0MiQ+ll4lMfgNV5d9javhQgzOJgXWUQ/OA+igrz5ORZadQGGRgk4solW+o/rZWuweqgXCpJFmjj4e+i1UgJrUjlxxd4zu4h8lNyoRsxUyMvMsG4XZANxr1Ca9cbz9jawXM94QJwnuqjY2w5Dg4ssO7YwIZo6lP3WLokxjbTO8nwPYEnLBsO/P1r9qE1n1w3UV0xxpNZaLq7LWJRTpEksyKYGPtv7QmbrOQ/k+Khy5MU+CnsINrLxJiHfOtBPbEQw1sHkz86lTudw5GKipWs7qkaz1C+h1vTW3vtJ0lTqs3RZLUx9bJpaaEDrJneExnXeBiNgU3wO2X4g6QeRaZIprL/1/+FomemJUoBvALjkiimA8WZDUnhJpOGPz5Q6xe3C9e2sFHcYZqkd66ky2qUIdMIkSMZ1mVDUTjEQ8RYNQMJogkSWwVUa/7nJmADuzJmGFDjN4ooRqXx1I+9J1j/WTdfEss+KNu0zuNbAJ3fcGVjs9y6StfxMRSwmf/VNdm+52cfLnnhnFguoCbgHs7d01JZv7H+AmH2VPyOEi47/hY964HW4HsXrYHWIspUCHYhT0BZmtOZHtmdpZOhiC0r8BQZ0A7D0jgJWxI85ZMgJNnKuRtoLSZ3dLImzIeDsJYvf4D3KTIWPvWCYJCJfBbhs1vvKnuwsUB/HA0W3RC9mvv5EwGL+2XNryVg5v6XLNWP+576p0HLr2QwOWYvbypplmxY9HgYItyllMod3F1mE8+Akyzt5+C+xLu0xoD5sBuyxs/IrQ29KRWjWT6jE8KSVZMULK3Qo7f3r8TCmnmmAGEWHMONuHhNSbr0EWPBcdffSZqAtHcgitZpk0afs4ek+R8BI2tSzgqEsBMumxIPRhKzQ55NuZ6cJz4yb8tq/MU47Isxvbv8F9TB5Gk8RP5fjNWcli/2Vjnx/9lRgsSw2YHzMDuRArqANGQgcH5+UyXXq4cub37/vHK4wUY+oMMm64r5TxiGGvCJJ4J6bHpl0kR/JM/v9I6DJwFr7YnHCnHOJTl5yVgAjO6LTfBNvFoMqCyOb0VInaIXAVQ98ZzhHLuArIvafyj+lXzJLDv/fQ3ZHuzoeg9FHm3os1YAdiBZO0nkkFPvWXT9BQQSK1unwwnBXGrDU1RBa74W5pAVBFXM+HuRmq7zpTZl/iiES3CRd+0oVmUSwJeeu2/b6GhiJKFmVp9TjERDydON8fUk3y7LRNAKaBAROX5zShUCuTADxUrylbLAUMd3Cp0gNO2lFTp3xZYw1I5jgkZmCtNIOEiPUFZn9aXguzqerZmzQktNmP8u9jVETkAnPD106+nCbMADn+9BFEPFU2E14Vz90/gWZST89ClkjEDruSh7ZQbVv1CbWkx53dGv7S3YNiW1TfiEwaJWKlbYlRtkOJYVLTCULPUUK1B8wzaogXJWpNA/ymODzxiOwuqhmLUH3jYtiGrp9VZl/gDD1IDlh0kLpXlnz9iJIZmZ/9GL8LTuom+ws5nDDtOl1ORPWawudMdfB1+3sLc2d9BRuNy+d2HWmx8BwFdwmWRyMlGRcMZ5obURSqdCFSQWhjaS1E/vO41XZqyn/PSD02MAGkQvscIkZl32plvrPO3sjo0qbZHccI6PufPZTbeZtWbkVbUUwi1gtKOXpQn93Spju5kNuBEez0skol5euLr9hMZn9hR6lknK//fz+0o65PCFFFAEaaQncEPXBHasuDSQKdozy1HX0hqeircuJ5v/rGM8BOehMi7VTbAVhQeaVkJTFgNXpzgoBYvU5L6aCnyD95eV7jCiyixqPOf0QkOm9KGUeX6lly1ZAdVHuNWz/DYp6oA2EBuJOLsGc/LzM+SvtRetYGIQ/PrLYhA5QYEJ+tvBMO3ibL8/ukmiZi6qpBFM0LsJkjx23AaBZypWUKSPs3efYd2ha1TaTL6JOLqqtTb0FyNulwbJQ2DkQR+79ymch2jz9N4V726TqQq2k9CH5ie4AtM3q2pdQA1bFBHDsb46NjUlUCYKNZt3K+FpxgXcPW+k5X8QnPdh6tDsZ6HmS5bcVHaDpHxQ6WqquMsClZz79cGDJT3E2t9tv566HG9mbrZShmkqrWvJEf46m2gAN4jjvAdnA5IwF5peGeqBw61m1v63MSvsFCYXnvr6lP23k0kLqWgdGhCHgYs8UL6tEN8ghGmlxmkFO3zrFWp/yCaX0UvOkm8FooJw3H5y1OsXFGJvPYG3VGZGlrxCC0AYzFlV5gSap+2tu8ZF1EcuzNyWH3jECoAExPmj+WJP6Mv+kitLoAMmzgMqlXZNscBsvZtRRg9wvLtfWlj148nawICvQ3Wo/XSPQYve/dZFqSJd4Y0WPGMV3x9bzHlVOV2B2SW+O8wMNcL5PcdmjDOOwqhYxnEaU5YKd6R4sfjcoawFThhfDmGRgugAAc4x72vcITP8pejr8rJM2+9NnloW/yKdfylMr/eOqYhrUfkfoIIH5LcbRhU7o62Seyt1vMp2EkZYCCD4GrwcQZN7hLyq1FpQPx8EWYYykHLASVjChzX6JPnGposON7v+OgvE4Zxn40kgYUz1aDa36upfJH1NnNTDIFvHefERpylhFRYePha+c1hZUQ1d3a6jUO8vBnAVt3GNhCdqbZhgBWVHFO2mSRExXO643vvBsNrJgio5lGulsFUPsBvc/M/ylHVZtjetOQyp+nBKhhx86aIuQt3NkUmqXY9LXW7Qylg2KHmCGomsVsV05tCARoChh9yq8tz8/UZIEfQ1wHXs5xXSXFxCC3CUZZIDoo1rFzBKF8dwxR57s/v1EXvEK7KDxlCSad9/oOv0Fs3n8Aeio6Cl+kmzeNkPz38mKpVfeT8qRLKbQL4VpTBwRUr/GvRApMmhzX1jbwXZ73Gdwara85ObyoCe4BamlbPIr4AtHG3bIymZ51qBsehntA5xP7HtpeUNIh/jmBR6JkH5kyuu3EnOmT28C6inXhJbfyqQGgrIkCdT2qk40B7ZEn+Dh6aiYiFp7snDa65smH+rkY4DAk2EqKyw91hWmtzNLOstKlgele+LDpKeYwEX8ehs4TrobeJWmo1gFHdI5f5iZ/wLhajPWkoqWEFtfZ81A/5IQspskTV0/D35whCBLW8AY+8sqYjC3aPB9seIXKsVEmaePITbbShmHyFBg0D5EfhQTagAdQ4L0USLvQpwz1vla48ec4MTfgX/pLFNc3jThOv9axXgR/YPxoD7dOTITqZ/Z5PwNSraA9sSZvYpU4ENhVSJQzq/oktAqARiX1T6E/abjfW833rfrEKQb1iGFHkiN7asqFhy5WHwp+brEGETeAjUeEfR3GYcbPATOIQipRP1UZd/LGZIKaH6xXcBDy/Q03iadPbylzeUF",
            "__VIEWSTATEGENERATOR":"FE27D343",
            "Editor$Edit$txbTitle":"23456",
            "Editor$Edit$EditorBody":"<p>23456</p>",
            "Editor$Edit$Advanced$ckbPublished":"on",
            "Editor$Edit$Advanced$chkDisplayHomePage":"on",
            "Editor$Edit$Advanced$chkComments":"on",
            "Editor$Edit$Advanced$chkMainSyndication":"on",
            "Editor$Edit$Advanced$txbEntryName":"",
            "Editor$Edit$Advanced$txbExcerpt":"",
            "Editor$Edit$Advanced$txbTag":"",
            "Editor$Edit$Advanced$tbEnryPassword":"",
            "Editor$Edit$lkbDraft":"存为草稿"
        }
        r2 = s.post(url,data=body)
        if "postid" in r2.url:
            print("随笔保存成功！")
            print(r2.url)
            postid = re.findall("postid=(.+?)&actiontip",r2.url)[0]
            return postid
        else:
            print("随笔保存失败!")

    def bky_delete(self,postid):
        """博客园——删除随笔"""
        url = "https://i.cnblogs.com/post/delete"
        body={
            "postId":postid
        }
        r3 = s.post(url,json=body)
        # r3 = s.post(url,data=json.dumps(body))
        isSuccess = r3.json()["isSuccess"]
        if isSuccess:
            print("删除成功！")
            return True
        else:
            print("删除失败！")
            return ""

if __name__ == '__main__':
    s = requests.session()
    g = BkyLiuCheng(s)    # 类的实例化，类是需要实例化的
    g.bky_login()         # def函数：实际就是class类的一个方法
    postid = g.bky_save()
    result = g.bky_delete(postid)
    print(result)

'''
函数：是具体的过程，面向过程
  类：是抽象的对象，面向对象
'''