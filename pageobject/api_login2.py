from common.apibase import ApiBase
api = ApiBase()

class Login():
    def login(self, username, password):
        """百度网登录"""
        url = "https://passport.baidu.com/v2/api/?login"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "alg": "v3",
            "apiver": "v3",
            "callback": "parent.bd__pcbs__nsef9n",
            "charset": "UTF-8",
            "codestring": "",
            "countrycode": "",
            "crypttype": "12",
            "detect": "1",
            "ds": "t0MQnv1sfh5VKt0p11CrEPE6zQ3SwNYtOeKcwT7Cs3t0ifpPw8kiPuJUF9ugaYqqpcszr58nENsbCSTgbGpCvg874I6xn+KS6TlM/Uh/vJq9DCW/elyh1nEvedsIDuIX0ljgHVAQNI8ypPSV+HaYTLfb0ENL+xtI2jtC1hHMT/EroGoCvyMOSlXCYKj367QS7Kb1Cbev74xG01XwIC7liEGxOzMb8aRcQz1omihLJFCVT0wsvqjbWe9497EAihS1F1mGzPk6O3YDSom4723ZXPLXqvmiw9vB76PmgPjJxf4c0FyeRK9HiEqUMQCa6eoQp2CwamD4dTC8jM+u3Bj7xTg+YwDm/CleZOdcsWzevgCUqdDzEJ9/YBu6NsQEdciJxaMckymiDtvjRCaNBon2JLoeK5HImVo/L/oUFlPC8mkVfKywR8d2GWOModHYRgvJQvJ2BYaIJXbUbmi2N+MCb922NiK71VXKxkpRoswGlWYJV0rZbi8qRA6qogqITSmcPdGxxvnNtgB0h4Ki+vO69UGxOzMb8aRcQz1omihLJFBWA+7zoFIu6+9qo3vTzFP6F1mGzPk6O3YDSom4723ZXIZjYDEpKPKoH2UYsl7rc4H8AggimJdagA2SX4yx0mgwljCqoKGeZ6YiwXomShSStxDEgfL+x6uEWZ/GMgfaeQq/SRvlqyhmQ4bjWO5eoIKK0Fit0HIyZzPBbKP/tbrmRRJ2oxVEYoqVYkRASV4mi4UIVuhfvJLTW4gut8Fz1+H1dtoXWxM4uxPZpwy3ficWCi6NsGSrpRb8rW0apA2lZAeyz/FvrlaOBTkKy2nDVOBKzD+p60p4aU2RC36bJr48949fctw5i47DRVhP2OtL07+Ieg9/wwIdEHFQ6kxJY+vC9nyl67FbgbDDxc6y9ZwYEHohRTRFdrQ3h/fLKw4d21Z2fy5rWcwxab4yDIYs8Rk3uS/Y+Jt2w17F/pBXOfJhgkv7jqzv7fJSQCbNDYsQqiiKjavToqIy3QYQ9ua/JRQVrcQZavd74tTHtp5SZ1Fc/WRPesrgWJGPOELJobvCrZgda6o7TmsIpdbcFfwV95NMLjjhgz9HZzJ/SnUqBPpMZDMdakHbT4S6QfNay3YRaNNS4Z8kjoG/+U0jZY3GAEV5",
            "dv": "tk0.63367566627866691624276992252@jjn0eIo2MYBmgnCnz4n3po0jyCnjh9Bvr90whNRwowJwr3AktxB2nF9kMjAkqYIsp8GjrhvIy9npoC0as~0jyFM0oaOxy~EmF~o2CF80FwB~FFApGhv3OHCnj90jhvnplgBQy9R5paRwOfR6CYB2Mj8khlo2UYBmgnCnz4n3po0jyCnjh9Bvr90whNRwowJwr3Aktx8ktF9kUjAkqYIsp8GjrhvIy9npoC0as~0jyFM0oaOxy~EmF~o23ZBcF_Xn0rjo2MaAktaB1FgokUgApGhv3OHCnj90jhvnplgBQy9R0r2JxGQ9kM~B1Fg8vnYB2Bz8mgnCnz4n3po0jyCnjh9oQy9O5QZJ5Ilo2qSAkCS8mFao2swA4FZ8kRYBHFZoangA4FaovRYovUgAktgB2BZA4F_IvvLzvFqqtZUhFnhBHFaAkUzEnrO5YFA2MaBaMwovMxo2tw8kMxo23go2tZB2Rx8v3~B2n~hn0RvL4GZR4BKA~yFM0oaR5y~Omz1MDQ3OHz2JxZfuxOQO4hNRwo~E0oQO4hwEmgjJ6GQE6QWEDC_Bn0jvBvRjAkMSBmFgB2sZAkMjB1Fg8vtFAksF8kqYBv3~BmFgB2CaAkUSoq__",
            "elapsed": "32",
            "fp_info": "",
            "fp_uid": "",
            "fuid": "FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD3iAJZpK/vamtTTGqdKc877l5HHJWRHU5zm61W/f6k61+uOF7slRVnnTywtGHmDpnMsv9IVv/yWrzTOpO5mzGl5hUHPBIGT6NWk6FePDbbfkQPtk9zYM/Chr0zJ1MGIs+XQ3W1SpqHdv7pl9cRHvSdGA5W5aWyRLiOlolyCGVS7qB1dYQJBVRgdi1KHBJ+Xl2UJeDHUs3GBB97C3qgUKwapVEoJ+QFRuKHbRqMpKP64xW8WivYeq15EPbJBsd8pf0sz7xwR33B2SKaONMlU7Qd5SVEqMA7i91JXBAq/w+5AHBJuha2lxeJ3S2WOi2rLOyJoUOZrcd5uQtC4RT7fkrJ2Uz4xFghCDCS+ftI/GwjAjsk8DkoZPyjVREjEk15uTix+MTCoPkvrKwfqhqJJ9YAirmZ2z+qA9DBNQqv8qCuXfk2892Of9sKu9wj25jjzeepEvovMcGFUKcWJi3mo5UR1uXDMvZlfbgHA09mSKeJ3rO21PLHqRbYEf/85IWzCuPyQT6E1WaBEFsnQj/EUosnZDB1kaYXuiqpWIT/jKcLYJNV/QRQpz9OxL2VppXiVh0IG4z5Iej5fHUmTzo7G7KQ35rG4+h0gsZ2eMGgzIHtuSdHSca1LKWVeMyCr4ln7C0PkrcO2LQsvV3n4P+zmS6m3SXHRNR7XTyRC4MK4DBC9S8YClTpPkuiWM0gZm41VCO+dj8pAfyVHqnsedsJI6TBEYbC8gI2kvgAwcX8u3AGA1NdaSkicteNd8nVRtJVPj3MPKhDvx2whiTp8oEUpL6vI85KLxuJHQCMrsXb4Z6QTnrXfL5SfEnaVo7kf2cacVxiUHSqbPo2PPJzEor12m6lThR7YgmlfLt7kntJD5XeM7GEQw3OLo5dsSUeQDd6vDnkb72/TMYcbPW48WuSnSgMDL820G6v5sII3fbIl1IswRGEQw3OLo5dsSUeQDd6vDntVllC1+aCCc8K28RWpYmU0S24R9DDZVx3j3+tLLpw3BRuF/lI7yGQ5dEntCEMtnVdtRt8uqdoWvVmS4FhMART4U5ZZ2QvNYYVj4McvsdmZl2ssb09Yk1KUaxhNd9iuw6w==",
            "gid": "35ACAFB-DDC8-4639-B4BC-B6E6BC18C4B7",
            "idc": "",
            "isPhone": "false",
            "loginmerge": "true",
            "logintype": "dialogLogin",
            "loginversion": "v4",
            "logLoginType": "pc_loginDialog",
            "mem_pass": "on",
            "mkey": "",
            "password": password,
            "ppui_logintime": "30693",
            "quick_user": "0",
            "rinfo": "{'fuid':'f6429a0639d1b7aebe69f006208d387a'}",
            "rsakey": "Jwmrv5aTVwRh36qrhBPxqZwlgzezqihT",
            "safeflg": "0",
            "shaOne": "00f0d27d01e3457e3f0bf2dace366897209a39b0",
            "sig": "bDJxL1hsSjBsbHYrcEY3dkJEd0JSSWFPSmZHVU01R3B6QXlpK3piL3AwU2RGajRmTmg2SExWR0hJR25XODEwSw==",
            "splogin": "rate",
            "staticpage": "https://passport.baidu.com/v3Jump.html",
            "subpro": "",
            "supportdv": "1",
            "time": "1624277022",
            "tk": "5388jLrQhq89v6y86sN4nD7DfX7Akzw1MUs83U42kSkrMOFmCSVJMu6kcasksEHpY6kcBBEGy0OrebH9ZbtXD49UPcr2RQz8q2i3c+wB+6zQPqI=",
            "token": "258eceae6267dc7d069122292dfac3a7",
            "tpl": "pp",
            "traceid": "7E845601",
            "tt": "1624277022486",
            "u": "http://passport.baidu.com/center",
            "username": username



        }
        res = api.post(url, data, headers=header)
        if res.status_code ==200:
            return True
        else:
            return False



if __name__ == '__main__':
    lg = Login()
    a = lg.login("16602710209", "czBNmItHv2K9pTMmX4IsGN/KU8BA69kkpEb/QSITu94l9D4cgYUotj14ZDsq8MEi6NNX3CfCxxDu5je48C4ZzG2STxUiF8qtF4TOH7aKCoTjpU2DNaChhoVin7lvZ/me9/gmiwntnqdfF0yGxNeDFZ5jaIGCaqU909aqdruTJ2Q=")
    print(a)