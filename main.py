import telebot
from telebot import types
import datetime
import logging
import os
from dotenv import load_dotenv,find_dotenv
import sqlite3
import time
from pyrogram import Client



#Load .env variables
load_dotenv(find_dotenv())
#print(os.getenv('TOKEN'))

#bot identity
TOKEN = os.getenv('TOKEN')
APP_ID=os.getenv('APP_ID')
APP_HASH=os.getenv('APP_HASH')
bot = telebot.TeleBot(TOKEN)
app = Client("my_bot")
version = "0.6.0"
totalgc = 1

#sqlite
#db_name = 'database.db'
def run_query(query):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()

'''
cur.excute()
from row in data:
    print(row)

#coomit buat manipulasi data
conn.commit()
conn.close()
'''

#setting log
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)



def log(message,commandText):
    tanggal = datetime.datetime.now()
    tanggal = tanggal.strftime('[%d %B %Y]')
    firstName = message.chat.first_name
    lastName = message.chat.last_name
    text_log='{},{},{},{}\n'.format(tanggal,firstName,lastName,commandText)
    log_bot = open('log.txt','a')
    log_bot.write(text_log)
    log_bot.close

@bot.message_handler(commands=['start'])
def send_welcome(message):
    log(message,'start')
    #memanggil inline keyboard
    markup = types.InlineKeyboardMarkup()
    btnContactOwner = types.InlineKeyboardButton('Pamsky.',url='t.me/impamsky')
    
    #assign tata letak keyboard
    markup.row(btnContactOwner)
    bot.reply_to(message,'Hallo, Sapu terbang siap mengantar pesan ke Group sebelah. \n/help untuk melihat bantuan.\nKalo masi bingung tanya creator',reply_markup=markup)

@bot.message_handler(commands=['version'])
def show_bot_version(message):
    log(message,'version')
    bot.reply_to(message,'Sekarang bot di versi\nv{}'.format(version))

@bot.message_handler(commands=['help'])
def send_help(message):
    log(message,'help')
    chat_id=message.chat.id
    bot.send_message(chat_id,'''List All Command :\n\nAmong Us Room\n/role \- Memasukkan Code Room\n/room \- Show room list\n/del \<code\> \- untuk menghapus code pada /list \n\nBirthday\n/ultah \- Untuk melihat list hari ulangtahun di group\n/setBirthday \- Untuk mengatur hari ulangtahun\n\nProfile\n/profile \- Melihat identitas kita\n\nMisc :\n/groupinfo \- Melihat info group\n\nGeneral\n/version \- Melihat versi bot''',parse_mode='MarkdownV2')

@bot.message_handler(commands=['role'])
def send_role(message):
    log(message,'role')
     #mengambil data chat
    chat_id=message.chat.id #id group
    
    texts = message.text.split(' ')

    if len(texts) <= 1:
        bot.send_message(chat_id=chat_id,text="Example :\n/role <Code> <Mode> <Host>\n/role abcdef normal ryu")
    else:    
        code = str(texts[1]).upper()
        mode = str(texts[2]).capitalize()
        host = str(texts[3])

        bot.reply_to(message,'Pesan di kirim ke {} group terdaftar.'.format(totalgc))

        #add code to database
        query = '''INSERT INTO room(code_room,mode,host,from_gc,is_public) VALUES('{code}','{mode}','{host}','{chat_id}','0')'''.format(code=code,chat_id=chat_id,mode=mode,host=host)
        run_query(query)

        #gc pam
        bot.send_message(chat_id=-1001826122574,text='**`{code}` `{code}`\n`{code}` `{code}`**\n☝Click code to copy☝\n\nMode : {mode}\nHost : {host}'.format(code=code,mode=mode,host=host),parse_mode='MarkdownV2')
        #gc au indo gc
        #bot.send_message(chat_id=-1001746697467,text='**`{code}` `{code}`\n`{code}` `{code}`**\n☝Click code to copy☝\n\nMode : {mode}\nHost : {host}'.format(code=code,mode=mode,host=host),parse_mode='MarkdownV2')
        #gc cucing
        #bot.send_message(chat_id=-1001765155506,text='**`{code}` `{code}`\n`{code}` `{code}`**\n☝Click code to copy☝\n\nMode : {mode}\nHost : {host}'.format(code=code,mode=mode,host=host),parse_mode='MarkdownV2')
        #gc idn -1001607301547
        #bot.send_message(chat_id=-1001607301547,text='**`{code}` `{code}`\n`{code}` `{code}`**\n☝Click code to copy☝\n\nMode : {mode}\nHost : {host}'.format(code=code,mode=mode,host=host),parse_mode='MarkdownV2')


@bot.message_handler(commands=['del'])
def send_role(message):
    log(message,'del')
    chat_id = message.chat.id
    texts = message.text.split(' ')
    code = str(texts[1]).upper()

    query = '''DELETE FROM room WHERE code_room="{}"'''.format(code)
    run_query(query)

    bot.send_message(chat_id,'Code _{}_ berhasil di hapus terdaftar'.format(code),parse_mode='MarkdownV2')

@bot.message_handler(commands=['roletest'])
def send_roletest(message):
    log(message,'roletest')

    #mengambil data chat
    chat_id=message.chat.id #id group
    
    texts = message.text.split(' ')
        
    code = str(texts[1]).upper()
    mode = str(texts[2]).capitalize()
    host = str(texts[3])


    
    bot.reply_to(message,'Pesan di kirim ke {} group terdaftar.'.format(totalgc))

    #add code to database
    query = '''INSERT INTO room(code_room,mode,host,from_gc,is_public) VALUES('{code}','{mode}','{host}','{chat_id}','0')'''.format(code=code,chat_id=chat_id,mode=mode,host=host)
    run_query(query)

    #gc pam
    bot.send_message(chat_id=-803823202,text='**`{code}` `{code}` `{code}`\n`{code}` `{code}` `{code}` \n`{code}` `{code}` `{code}`**\n☝Click code to copy☝\n\nMode : {mode}\nHost : {host}'.format(code=code,mode=mode,host=host),parse_mode='MarkdownV2')
    #bot.send_message(chat_id=-803823202,text='**`{code}`**\n☝Click code to copy☝\n\nMode : {mode}\nHost : {host}'.format(code=code,mode=mode,host=host),parse_mode='MarkdownV2')    

@bot.message_handler(commands=['register'])
def register(message):
    log(message,'register')
    #mengambil data chat
    chat_id=message.chat.id #id group
    
    #check id if has registered
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    data = cur.execute('''
        SELECT * FROM "group" where id_gc="{chat_id}"
    '''.format(chat_id=chat_id))
    if data.fetchone():
        print("Record ada")
        #for row in data:
        #   print('=============1')
        #    print(row)
        #    print('=============2')
        bot.send_message(chat_id,'Group sudah terdaftar sebelumnya')
        
    else:
        print("Record {} tidak ada dalam database")
        nama_gc = message.chat.title

        #if not register inserting query database
        query = 'INSERT INTO "group" (id_gc,nama_gc) values({chat_id},"{nama_gc}");'.format(chat_id=chat_id,nama_gc=nama_gc)
        run_query(query)
        print("Record {} berhasil di registrasi dalam database")

        #send massage if succes
        bot.send_message(chat_id,'Group ID : {} berhasil di daftarkan'.format(chat_id))
    conn.close()

@bot.message_handler(commands=['groupinfo'])
def info(message):
    log(message,'groupinfo')
    chat_id=message.chat.id
    memberCount=bot.get_chat_member_count(chat_id=chat_id)
    
    bot.reply_to(message,'Group ID : {chat_id}\nJumlah Member : {memberCount}'.format(chat_id=chat_id,memberCount=memberCount))

#Showing active Code Room Among us
@bot.message_handler(commands=['room'])
def show_list(message):
    log(message,'room')
    chat_id=message.chat.id

    

    #Check id chat
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    data = cur.execute('''
        SELECT * from "room" WHERE from_gc="{chat_id}";
    '''.format(chat_id=chat_id))
    record = data.fetchall()

    if record:
        print("Record ada")
        #bot.send_message(chat_id,'Kode Di Group Ini Saja\n') 
        isiRoomCode = str("List Room :\n")
        for row in record:
            print(row)
            code = row[1] #  mengambil code dari row
            mode = row[2]
            host = row[3]

            isiRoomCode = isiRoomCode + str("\n`{code}` {mode} {host}".format(code=code,mode=mode,host=host))
            

        print("Done loop")
        isiRoomCode = isiRoomCode + str("\n\nPencet kodenya untuk mengcopy")
        bot.send_message(chat_id,isiRoomCode,parse_mode='MarkdownV2')
        
        
        

    else:
        print("Record tidak ada")
        nama_gc = message.chat.title
        bot.send_message(chat_id,'Belum ada room tersedia. Silahkan membuat room. Bantuan membuat room /help')
    
    conn.close()

#if bot is added to group, this handler will work
@bot.my_chat_member_handler()
def my_chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member

    chat_id=message.chat.id #id group


    if new.status == "member":
        
        
        #check apa gc udah ada di database
        #mengambil data chat
        
        
        #check id if has registered
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        data = cur.execute('''
            SELECT * FROM "group" where id_gc="{chat_id}"
        '''.format(chat_id=chat_id))
        if data.fetchone():
            print("Record ada")
            #for row in data:
            #   print('=============1')
            #    print(row)
            #    print('=============2')
            bot.send_message(chat_id,'Eh udah terdaftar ya')
            
        else:
            print("Record {} tidak ada dalam database")
            nama_gc = message.chat.title

            bot.send_message(message.chat.id,"Apaan sih add add") # Welcome message, if bot was added to group
            bot.send_message(chat_id,'Group ID : {}\nNama : {} \n\nBelom ke daftar tau'.format(chat_id,nama_gc))
            bot.send_message(chat_id,'Bye...!!!')
            time.sleep(10)
            bot.leave_chat(message.chat.id) # command buat keluar dari group itu
        conn.close()

#Birthday List
@bot.message_handler(commands=['ultah'])
def ultah(message):
    log(message,'ultah')

    #Get varibale
    chat_id=message.chat.id
    text = message.text
    user_id=message.from_user.id
    print(user_id)


    #Check user apakah ada dalam database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    data = cur.execute('''
        SELECT * from "user" WHERE id_user="{user_id}";
    '''.format(user_id=user_id))
    record = data.fetchall()

    
    #If record found
    isiRoomCode = str("🎊🎉List Ulang Tahun🎉🎊\n")
    if record:
        print("Record ada")
        #bot.send_message(chat_id,'Kode Di Group Ini Saja\n')
        bot 
        
        for row in record:
            print(row)
            nama = row[1]
            mention = "["+nama+"](tg://user?id="+str(user_id)+")"
            tgl = row[2] #  mengambil code dari row
            bulan = row[3]
            tahun = row[4]

            isiRoomCode = isiRoomCode + mention + str(" {tgl}/{bulan}/{tahun}".format(tgl=tgl,bulan=bulan,tahun=tahun))
            #mengirim pesan dari olahan database
            bot.send_message(chat_id=chat_id,text=isiRoomCode,parse_mode="MarkdownV2")
    else:
        print("record tidak berhasil / tidak ada")
        isiRoomCode = isiRoomCode + "List Kosong"
        bot.send_message(chat_id=chat_id,text=isiRoomCode)
    
    

@bot.message_handler(commands=['profile'])
def show_profile(message):
    #Get variable
    chat_id=message.chat.id
    id_user=message.from_user.id
    firstName = message.from_user.first_name
    lastName = message.from_user.last_name
    userName = message.from_user.username

    #Check user apakah ada dalam database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    data = cur.execute('''
        SELECT * from "user" WHERE id_user="{id_user}";
    '''.format(id_user=id_user))
    record = data.fetchall()

    #If record found
    if record:
        print("Record ada")
        for row in record:
            print(row)
            tgl = row[2] #  mengambil code dari row
            bulan = row[3]
            tahun = row[4]

            #if tahun 0 makan jadi empty
            if tahun == 0:
                lahir = str(" {tgl}/{bulan}".format(tgl=tgl,bulan=bulan))
            else:
                lahir = str(" {tgl}/{bulan}/{tahun}".format(tgl=tgl,bulan=bulan,tahun=tahun))
            
    else:
        lahir = "/setBirthday"

    bot.send_message(chat_id=chat_id,text="ID : {id_user}\nFirst Name : {firstName}\nLast Name : {lastName}\nUsername : @{userName}\nBirthday : {lahir}".format(id_user=id_user,firstName=firstName,lastName=lastName,userName=userName,lahir=lahir))

@bot.message_handler(commands=['setBirthday'])
def setting_profile(message):
    #get variable
    chat_id = message.chat.id
    id_user= message.from_user.id
    text = message.text.split(' ')

    
    #If dont have parameter show help for birthday
    if len(text) <= 1 :
        bot.send_message(chat_id=chat_id,text="Example :\n/setBirthday dd mm yyyy\n/setBirthday 29 12\n/setBirthday 29 12 2020\n\n*tidak harus menyertakan tahun")
    else:
        #get data from text
        tgl = text[1]
        bulan = text[2]
        if len(text) <= 2:
            tahun = 0
            print("tahun tidak ada")
        else:
            try: 
                tahun = text[3]
            except:
                print("ada eror")
                tahun = 0

        nama = str(message.from_user.first_name) + str(message.from_user.last_name)
        print(nama)

        #check is user in database ?
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        data = cur.execute('''
            SELECT * from "user" WHERE id_user="{id_user}";
        '''.format(id_user=id_user))
        record = data.fetchall()

        if record:
            print("update")
        
        else:
            #if not register inserting query database
            query = 'INSERT INTO "user" (id_user,tgl_lahir,bulan_lahir,tahun_lahir) values({id_user},{tgl_lahir},{bulan_lahir},{tahun_lahir});'.format(id_user=id_user,tgl_lahir=tgl,bulan_lahir=bulan,tahun_lahir=tahun)
            run_query(query)
            #print("Record {} berhasil di registrasi dalam database")

            #send massage if succes
            bot.send_message(chat_id,'Tanggal Lahir Berhasil Di Ubah'.format(chat_id))
            
            #show profile after edited
            show_profile(message)
        


    
    

    

print('Bot Start Running')
bot.polling()
print('Bot Start Running 1')
app.run()
print('Bot Start Running 2')
