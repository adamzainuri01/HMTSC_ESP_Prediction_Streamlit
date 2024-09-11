import streamlit as st

pick_letter = st.selectbox(
    "Pick a letter",
    ("", "Review Botol", "HBD Rama 1", "HBD Rama 2"),
)

if pick_letter == "Review Botol":
    st.markdown("**Adam Zainuri: Pcr Ak**")

    st.markdown("**Botol – Vanguard Champion**")

    st.markdown("""
    Kali ini saya akan mereview pacar saya yaitu Adam Putra Pratama Zainuri. Lahir pada 14 Februari 2003, ia adalah seorang botol berusia 19 tahun yang di luar nalar. Tindakannya yang sulit ditebak membuatnya menarik dan mengantisipasi apa yang akan terjadi selanjutnya.
    
    Sehari-hari, gaya berpakaiannya santai dan cocok, seolah apapun yang dikenakannya akan terlihat bagus. Rambut ikalnya membuat saya berkeinginan untuk menyentuh dan membelainya. Hidung mancung serta rahang tajam pun turut menambah ketampanan wajahnya. Bahkan, tangannya saja pun sudah menarik, dengan ukurannya yang lebih besar dari saya sehingga tidak dapat menepis perasaan untuk menggenggamnya setiap saat.
    
    Sebagai pacar, Adam sangatlah oke. Kepekaannya serta kemampuannya untuk menghibur membuat saya tidak tenggelam dalam kesedihan. Memang, cara penyampaiannya yakni dengan komplain dan menegur menimbulkan rasa yang kurang enak, namun apa yang ia katakan benar adanya. Dia juga memberi rasa nyaman terutama ketika saya berada di pelukannya, seakan ingin waktu berhenti agar dapat terus bersamanya. Keharumannya pun dapat menjadi obat tidur yang efektif. Tidak hanya itu, dia juga dapat memberi kenikmatan dengan baik. Namun, terkadang ia terlalu agresif. Saya sama sekali tidak keberatan apabila hal tersebut dilakukan di tempat yang sudah pasti aman dan bebas gangguan saja.
    
    Terlepas dari ketika bersama saya, Adam memiliki pesonanya sendiri. Kepintaran, cara bertindak, maupun suaranya yang keren namun lembut membuat saya tertarik padanya. Ia juga jago dalam bermain berbagai game dan kartu, yang tentunya menambah kekerenannya.
    
    Secara keseluruhan, saya senang bersama dengannya dan ingin dekat dengannya.
    """)

elif pick_letter == "HBD Rama 1":
    st.markdown("**Buat Rama Sayang**")

    st.markdown("""
    Makasih banyak udah hadir di hidup aku. Aku seneng banget & bersyukur udah ketemu kamu. Kadang aku heran, kok bisa ada orang kayak kamu. Kamu yang peduli, bisa ngehibur, selalu ada, baik, pinter, ganteng, [redacted], lucu, keren, bikin pengen liatin kamu terus sm makin suka tiap hari. 
    
    Kamu yang bisa adaptasi, jago main game apa aja entah fisik ato digital itu keren banget buatku. Kak sebut namaku, aku ngefans. Aku suka kamu yang meluk aku erat, nempel ke aku, senyum, nyium kening aku, megang tanganku kalo lagi di motor (tp bahaya), manggil aku, mau nyelesaiin masalah, ngabarin, trs yang waktu aku sakit juga itu aku masih kagum sm kamu kok bisa & berani. 
    
    Makasih udah sabar ngadepin aku, nemenin aku, bantu aku kalo kenapa-napa, nganterin aku kemana-mana, milih dan nerima aku. Maaf aku sering bikin kamu ngerasa gaenak, bikin bingung, gajelas, banyak kurangnya. Semoga kita bisa ngelewatin banyak hal dan bisa bareng terus sampe akhir dan seterusnya. 
    
    Buat kamu, semoga sehat terus, rezekinya lancar, panjang umur, semua urusannya dipermudah, nggak banyak stress & sedih, keinginannya dikabulin, pokoknya semua yang terbaik buat kamu. 
    
    **Happy birthday Rama**
    
    **Aku sayang kamu**
    
    **Yaya ❤️**
    """)

elif pick_letter == "HBD Rama 2":
    st.markdown("**Hari RAMA, 2024**")

    st.markdown("""
    3 alasan kenapa Yaya pilih luar angkasa
    1. Rama kayak malem, dingin gelap tapi bikin tenang nyaman dan tetep bersinar bahkan lebih indah dari siang
    2. Nama Yaya ada di luar angkasa dan emang dinamain dari situ, biar rama inget Yaya terus
    3. Yaya suka bareng Rama aaplagi kalo malem, nikmatin dinign malem tapi tetep ngerasa anget dari Rama sama bisa ngerasa aman karena ada Rama
    
    Apakah Rama peyek paham?
    
    Makasih Sayang udah tetep sama aku tahun ini, semoga kedepannya aku bisa rayain ultah Rama terus soalnya Rama spesial wajib rayain hari Rama sedunia (Ramanya cuma punya Yaya tapi)
    
    Rama itu hebat, keren, ganteng, baik, peyek, sabar, jago, bocil, pinter, lucu, mambu, anget, perhatian, gemesin, bikin sayang
    
    Yaya suka bareng Rama, meluk ngelus ngelus, digandeng, dipeluk, dianter jemput, dihibur, didenger, disayang Rama, suka Rama peyek pokoknya
    
    Makasih banyak Rama kamu selalu berusaha mahamin aku, berusaha banyak buat aku sama kita
    
    Semoga urusannya selalu dipermudah, rezekinya lancar, sehat selalu, keinginannya terkabul, lancar sidang dan S2, pokoknya banyak dan aku yakin kamu bisa lakuin semua yang kamu mau
    
    **Happy birthday Rama**
    
    **Yaya sayang Rama**
    """)