import streamlit as st
import numpy as np
import pandas as pd

from PIL import Image
image = Image.open("pngegg.png")

st.set_page_config(
    page_title="DİYABET TAHMİNCİSİ",
    page_icon=image,
    menu_items={
        "Get help": "mailto:mustafaatak3435@gmail.com",
        "About": "For More Information\n" + "https://github.com/farabiatak"
    }
)
st.title('Diyabet Sınıflandırma Projesi ')
st.markdown("Veri setide 253.680 değer bulunmakla beraber,Veri Amerika Birleşik Devletlerinde toplanmıştır. ")
st.image("https://www.drerolvural.com/wp-content/uploads/2020/07/diyabet-kalp.jpg")

st.header('Bilgilendirme')


st.markdown('                                                                                       ')
st.markdown('                                                                                       ')
st.markdown('Eğitim : 1 - Okur-Yazar , 2 -İlkokul , 3 - Ortaokul , 4 - Lise , 5 - Yüksekokul , 6-Üniversite')
st.markdown('                                                                                       ')
st.markdown('                                                                                       ')

st.markdown('Gelir : 1 - 8600 ve altı , 2 - 8600 - 13000  , 3 - 13001 - 16000  4 - 16001 - 19000')
st.markdown('Gelir : 5 - 19001 - 22000 , 6 - 22001 - 25000 , 7 - 25001 - 28000 , 8 - 28000 ve üzeri')
st.markdown('                                                                                       ')
st.markdown('                                                                                       ')

df = pd.read_csv("diyabet_veri_tr_2.csv")
del df[df.columns[0]]
del df[df.columns[0]]
st.table(df.sample(5, random_state=13))

st.sidebar.markdown('Bilgilerinizi giriniz')

name = st.sidebar.text_input('İsim', help = 'Lütfen büyük harfle giriniz!')
surname = st.sidebar.text_input('Soyisim',help = 'Lütfen büyük harfle giriniz!')
boy= st.sidebar.number_input('Boy -- m',min_value=1.1)
kilo = st.sidebar.number_input('Kilo -- kg',min_value=20)
vke = (kilo/(boy*boy))
########################
htans= st.sidebar.checkbox('Hipertansiyon Teşhisi')
if htans == False :
    htans == 0
else :
    htans == 1
########################
kolestrol_kronik = st.sidebar.checkbox('Kronik-Kolestrol')
if kolestrol_kronik == False :
    kolestrol_kronik == 0
else :
    kolestrol_kronik == 1
#########################
kolestrol_teshis = st.sidebar.checkbox('Son 3 Yılda Yüksek Kolestrol Tespiti' )
if kolestrol_teshis == False  :
    kolestrol_teshis == 0
else :
    kolestrol_teshis == 1
#########################
sigara = st.sidebar.checkbox('Sigara Kullanımı')
if sigara == False: 
    sigara == 0
else :
    sigara == 1
#########################
inme = st.sidebar.checkbox('İnme,Felç,Kısmi Felç,Yüz Felci')
if inme == False :
    inme == 0
else :
    inme == 1
########################    
chd = st.sidebar.checkbox('Damar Tıkanıklığı')
if chd == False :
    chd == 0
else :
    chd == 1
########################
fizik_ak = st.sidebar.checkbox('Fiziksel Aktivite')
if fizik_ak == False :
    fizik_ak == 0 
else :
    fizik_ak == 1
#######################
meyve = st.sidebar.checkbox('Meyve Tüketimi')
if meyve == False :
    meyve ==0 
else :
    meyve == 1
#######################
sebze = st.sidebar.checkbox('Sebze Tüketimi')
if sebze == False :
    sebze == 0
else :
    sebze == 1
######################
alkol = st.sidebar.checkbox('Düzenli Alkol Tüketimi  --  (0 = VAR) (1 = YOK)')
if alkol == False :
    alkol == 1
else :
    alkol == 0
###################### 
saglik_sig =  st.sidebar.checkbox('Sağlık Sigortası')
if saglik_sig == False :
    saglik_sig  == 0 
else :
    saglik_sig == 1
######################
tedavi_reddi = st.sidebar.checkbox('Tedavi Reddi')
if tedavi_reddi == False :
    tedavi_reddi == 0
else :
    tedavi_reddi == 1
################3
merdiven = st.sidebar.checkbox('Merdiven İnip Çıkarken Zorluk')
if merdiven == False :
    merdiven == 0
else :
    merdiven == 1
#####################
genel_saglik = st.sidebar.selectbox('--------------------------  Genel Sağlık -------------------------      1 = Harika 5 = Berbat',[1,2,3,4,5])
#####################  
cins = st .sidebar.selectbox('------------------------------ Cinsiyet -------------------------------      1 = Erkek  0 = Kadın',[1,0])
######################
yas = st.sidebar.number_input('Yaş')
if yas < 18 :
    yas=0
elif 18 <= yas < 24 :
    yas = 1
elif 24 <= yas < 29 :
    yas = 2
elif 29 <= yas < 34 :
    yas = 3
elif 34 <= yas <39 :
    yas = 4
elif 39 <= yas <44 :
    yas = 5
elif 44 <= yas <49 :
    yas = 6
elif 49 <= yas <54 :
    yas = 7
elif 54 <= yas <59 :
    yas = 8
elif 59 <= yas <64 :
    yas = 9
elif 64 <= yas <69 :
    yas = 10
elif 69 <= yas <74 :
    yas = 11
elif yas > 74 : 
    yas = 12 
else :
    yas = 12    
       
egitim = st.sidebar.selectbox ('Eğitim Durumu (1 - 6) - Yukarıdan Eğitim Skorunuzu Görebilirsiniz',[1,2,3,4,5,6])
gelir = st.sidebar.selectbox ('Gelir Durumu (1 - 8) - Yukarıdan Gelir Skorunuzu Görebilirsiniz',[1,2,3,4,5,6,7,8])
ruhsal = st.sidebar.selectbox ('Ruhsal olarak kendinizi son 1 ay içinde kaç kere kötü hissettiniz ?',[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
fiziksel =  st.sidebar.selectbox ('Fiziksel olarak kendinizi son 1 ay içinde kaç kere kötü hissettiniz ?',[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])


from joblib import load

logreg_model = load('logreg_model.pkl')


input_df = pd.DataFrame({ 
    
    'hipertans': [htans],
    'kolestrol' : [kolestrol_kronik],
    'kolestrol_check': [kolestrol_teshis],
    'vke': [vke],
    'sigara': [sigara],
    'inme' : [inme],
    'chd' : [chd],
    'fiziksel_aktivite' : [fizik_ak],
    'meyve':[meyve],
    'sebze': [sebze],
    'agir_alkol': [alkol],
    'saglik_sigortasi' : [saglik_sig],
    'doktor_vaz': [tedavi_reddi],
    'genel_saglik' : [genel_saglik],
    'ruhsal' : [ruhsal],
    'fiziksel': [fiziksel],
    'yuruyus_merdiven' : [merdiven],
    'cinsiyet' : [cins],
    'yas' : [yas],
    'egitim': [egitim],
    'gelir' : [gelir]
    
})


pred = logreg_model.predict(input_df.values)
pred_prob = np.ravel(logreg_model.predict_proba(input_df))
pred_prob_1 =pred_prob[0]
pred_prob_2 = int(pred_prob[1]*100)

st.markdown('SONUÇ')

if st.sidebar.button("Hesapla") :

    st.info("Bilgilerinizi girerek risk hesaplayabilirsiniz")
    
    from datetime import date,datetime
    
    today = date.today()
    time = datetime.now().strftime("%H:%M:%S")
    
    result_df = pd.DataFrame({
    'İSİM' : [name],
    'SOYİSİM' : [surname],
    'TARİH' : [today],
    'SAAT' : [time],
    'TAHMİN' : [pred],
    #'Olasılık'  : [pred_prob_1],
    'Diyabet Riski %'  : [pred_prob_2]   
    })
    
    result_df["TAHMİN"] = result_df["TAHMİN"].apply(lambda x: str(x).replace("0","sağlıklı"))
    result_df["TAHMİN"] = result_df["TAHMİN"].apply(lambda x: str(x).replace("1","hastalıklı"))
    
    st.table(result_df)
    
    if pred == 1:
        st.image('https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-81b7de06-af33-437a-8370-456e0590011f.jpg')
    else:
        st.image('http://www.verita.com.tr/wp-content/uploads/2014/08/girl2.jpg')
else : 
    st.markdown('Hesapla Butonuyla Sonucu Görebilirsiniz')





