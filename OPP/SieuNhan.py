class SieuNhan:
    suc_manh=50;
    stt=1;

    def __init__(self, para_ten, para_mau):
        self.ten = para_ten
        self.mau = para_mau
        self.stt += SieuNhan.stt + 1
    def xin_chao(self):
        return "helo:  " + self.ten

SieuNhan_A = SieuNhan("Gao Do","Den")
SieuNhan_B = SieuNhan("Gao Do","Den")
SieuNhan_A.xin_chao
print(SieuNhan_A.stt)
print(SieuNhan_B.stt)
print(SieuNhan.stt)
    