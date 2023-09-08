from django.shortcuts import render
from .models import feature,price
# Create your views here.
def home(request):
    feat1=feature()
    feat1.img="features/f1.png" 
    feat1.h='Free shiping'

    feat2=feature()
    feat2.img="features/f2.png" 
    feat2.h='Online order'
    
    feat3=feature()
    feat3.img="features/f3.png" 
    feat3.h='Save money'

    feat4=feature()
    feat4.img="features/f4.png" 
    feat4.h='Promotions'

    feat5=feature()
    feat5.img="features/f5.png" 
    feat5.h='Happy sell'

    feat6=feature()
    feat6.img="features/f6.png" 
    feat6.h='F24/7 support'

    feat=[feat1,feat2,feat3,feat4,feat5,feat6]  

    product1=price()
    product1.price=1000
    product1.img='products/f1.jpg'
    product1.Tshirt='Cartoon printed Tshirt'

    product2=price()
    product2.price=1000
    product2.img='products/f2.jpg'
    product2.Tshirt='Cartoon printed Tshirt'

    product3=price()
    product3.price=1000
    product3.img='products/f3.jpg'
    product3.Tshirt='Cartoon printed Tshirt'

    product4=price()
    product4.price=1000
    product4.img='products/f4.jpg'
    product4.Tshirt='Cartoon printed Tshirt'

    product5=price()
    product5.price=1000
    product5.img='products/f5.jpg'
    product5.Tshirt='Cartoon printed Tshirt'

    product6=price()
    product6.price=1000
    product6.img='products/f6.jpg'
    product6.Tshirt='Cartoon printed Tshirt'

    product7=price()
    product7.price=1000
    product7.img='products/f7.jpg'
    product7.Tshirt='Cartoon printed Tshirt'

    product8=price()
    product8.price=1000
    product8.img='products/f8.jpg'
    product8.Tshirt='Cartoon printed Tshirt'

    product9=price()
    product9.price=1000
    product9.img='products/n1.jpg'
    product9.Tshirt='Cartoon printed Tshirt'


    pro=[product1,product2,product3,product4,product5,product6,product7,product8,product9]
    return render(request,'home.html',{'feats':feat,'pros':pro})
