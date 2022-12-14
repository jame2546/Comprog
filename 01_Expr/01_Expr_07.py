def mosteller(w, h):
    return ((w*h)**0.5)/60
def du_bois(w, h):
    return  0.024265*w**0.5378*h**0.3964
def fujimoto(w, h):
    return 0.008883 * (w**0.444) * (h**0.663)
def main():
 weight = float(input())
 height = float(input())
 mos = mosteller(weight,height)
 bois = du_bois(weight,height)
 fuji = fujimoto(weight,height)
 print("Mosteller =", round(mos, 5))
 print("Du Bois =", round(bois, 5))
 print("Fujimoto =", round(fuji,5))
exec(input()) 
