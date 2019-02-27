# # -*- coding: UTF-8 -*-

##############################################################################
#                                                                            #
# Copyright (c) 2007-2010 Bernd Kreuss <prof7bit@gmail.com>                  #
#   Modifications and updates Copyright                                      #
# Copyright (c) 2014-2019  M. Weigand       <doctortor@use.startmail.com>    #
#                                                                            #
# Translation file for TorChat                                               #
#                                                                            #
##############################################################################

LANGUAGE_CODE = u"sv"
LANGUAGE_NAME = u"Svenska"
LANGUAGE_NAME_ENGLISH = u"Swedish"
TRANSLATOR_NAMES = [u"Åke Engelbrektson"]

#buttons
BTN_CANCEL = u"Avbryt"
BTN_OK = u"OK"
BTN_SAVE_AS = u"Spara som..."
BTN_CLOSE = u"Stäng"

#status
ST_AVAILABLE = u"Tillgänglig"
ST_AWAY = u"Frånvarande"
ST_EXTENDED_AWAY = u"Utökad frånvaro"
ST_OFFLINE = u"Offline"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = u"Visa/Dölj TorChat"
MTB_QUIT = u"Avsluta"

#popup menu
MPOP_CHAT = u"Chatta..."
MPOP_SEND_FILE = u"Sänd fil..."
MPOP_EDIT_CONTACT = u"Redigera kontakt..."
MPOP_DELETE_CONTACT = u"Ta bort kontakt..."
MPOP_SHOW_OFFLINE_MESSAGES = u"Visa köade offline-meddelanden"
MPOP_CLEAR_OFFLINE_MESSAGES = u"Rensa köade offline-meddelanden"
MPOP_ACTIVATE_LOG = u"Aktivera loggning till fil"
MPOP_STOP_LOG = u"Stoppa loggning"
MPOP_DELETE_EXISTING_LOG = u"Ta bort befintlig loggfil"
MPOP_DELETE_AND_STOP_LOG = u"Ta bort logg och stoppa loggning"
MPOP_ADD_CONTACT = u"Lägg till kontakt..."
MPOP_ABOUT = u"Om TorChat"
MPOP_TIPJAR = u"TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = u"Fråga %s..."
MPOP_SETTINGS = u"Inställningar..."
MPOP_EDIT_MY_PROFILE = u"Redigera min profil..."

#chat window popup menu
CPOP_COPY = u"Kopiera"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = u"Bekräfta borttagning"
D_CONFIRM_DELETE_MESSAGE = u"Vill du verkligen ta bort den här kontakten?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = u"TorChat: Loggning är aktiverad"
D_LOG_WARNING_MESSAGE = u"Loggning till fil är aktiverad!\n\nLoggfil: %s\n\nGlöm inte att ta bort loggfilen när du har avslutat felsökningen. Loggfilen kan innehålla känslig information."

#warning about used port
D_WARN_USED_PORT_TITLE = u"TorChat: Porten används redan"
D_WARN_USED_PORT_MESSAGE = u"Något, troligen en annan TorChat-instans, lyssnar redan på %s:%s. Du måste skapa en profil till, som använder andra portar, för att kunna starta TorChat en andra gång."

# #warning about unread messages
D_WARN_UNREAD_TITLE = u"TorChat: Olästa meddelanden"
D_WARN_UNREAD_MESSAGE = u"Det finns olästa meddelanden.\nDom kommer att förloras för alltid!\n\nVill du verkligen avsluta TorChat nu?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = u"TorChat: Kontakten är offline"
D_WARN_BUDDY_OFFLINE_MESSAGE = u"Denna åtgärd fungerat inte med frånkopplade kontakter"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = u"TorChat: Flera filer"
D_WARN_FILE_ONLY_ONE_MESSAGE = u"Du kan inte skicka flera filer i en och samma överföring. Skicka filerna en och en, eller packettera dom i en zip-fil"

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = u"TorChat: Kan inte spara fil"
D_WARN_FILE_SAVE_ERROR_MESSAGE = u"Filen '%s' kunde inte skapas.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = u"TorChat: Filen finns redan"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = u"Filen '%s' finns redan.\nVill du byta ut den?"

#dialog: add/edit contact
DEC_TITLE_ADD = u"Lägg till ny kontakt"
DEC_TITLE_EDIT = u"Redigera kontakt"
DEC_TORCHAT_ID = u"TorChat-ID"
DEC_DISPLAY_NAME = u"Visningsnamn"
DEC_INTRODUCTION = u"Introduktion"
DEC_MSG_16_CHARACTERS = u"Adressen måste vara 16 tecken lång, inte %i."
DEC_MSG_ONLY_ALPANUM = u"Adressen kan bara bestå av siffror och små bokstäver"
DEC_MSG_ALREADY_ON_LIST = u"%s finns redan i din lista"

#dialog: edit my profile
DEP_TITLE = u"Redigera min profil"
DEP_NAME = u"Namn"
DEP_TEXT = u"Text"
DEP_SET_AVATAR = u"Ange avatar"
DEP_REMOVE_AVATAR = u"Ta bort avatar"
DEP_AVATAR_SELECT_PNG = u"Välj en .png-fil som din avatar (kommer att skalas om till 64x64px, får innehålla transparens)"
DEP_PNG_FILES = u"PNG-filer"
DEP_ALL_FILES = u"Alla filer"
DEP_WARN_TITLE = u"Filen kan inte användas som avatar"
DEP_WARN_IS_ALREADY = u"Den här bilden är redan din avatar"
DEP_WARN_MUST_BE_PNG = u"Avataren måste vara en .png-fil"

#file transfer window
DFT_FILE_OPEN_TITLE = u"Sänd fil till %s"
DFT_FILE_SAVE_TITLE = u"Spara fil från %s"
DFT_SEND = u"Sänder %s\ntill %s\n%04.1f%% (%i av %i byte)"
DFT_RECEIVE = u"Tar emot %s\nfrån %s\n%04.1f%% (%i av %i byte)"
DFT_WAITING = u"väntar på anslutning"
DFT_STARTING = u"startar överföring"
DFT_ABORTED = u"överföring avbruten"
DFT_COMPLETE = u"överföring slutförd"
DFT_ERROR = u"fel"

#settings dialaog
DSET_TITLE = u"TorChat konfiguration"
DSET_NET_TITLE = u"Nätverk"
DSET_NET_ACTIVE = u"aktiv"
DSET_NET_INACTIVE = u"inaktiv"
DSET_NET_TOR_ADDRESS = u"Tor proxy-adress"
DSET_NET_TOR_SOCKS = u"Socks-port"
DSET_NET_TOR_CONTROL = u"Kontrollport"
DSET_NET_OWN_HOSTNAME = u"Eget TorChat-ID"
DSET_NET_LISTEN_INTERFACE = u"Lyssningsgränssnitt"
DSET_NET_LISTEN_PORT = u"Lyssningsport"
DSET_GUI_TITLE = u"Användargränssnitt"
DSET_GUI_LANGUAGE = u"Språk"
DSET_GUI_OPEN_MAIN_HIDDEN = u"Starta minimerad"
DSET_GUI_OPEN_CHAT_HIDDEN = u"Öppna inte nya fönster automatiskt"
DSET_GUI_NOTIFICATION_POPUP = u"Popupmeddelande"
DSET_GUI_NOTIFICATION_METHOD = u"Meddelandemetod"
DSET_GUI_FLASH_WINDOW = u"Blinka med fönster vid nytt meddelande"
DSET_MISC_TITLE = u"Diverse"
DSET_MISC_TEMP_IN_DATA = u"Lagra temporära filer i programmappen"
DSET_MISC_TEMP_CUSTOM_DIR = u"Temp-mapp (lämnas tom för systemstandard)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = u"Fördröjda meddelanden som väntar på att skickas "
NOTICE_DELAYED_MSG_SENT = u"fördröjda meddelanden har skickats"
NOTICE_DELAYED = u"fördröjd"

#messagebox for offline messages
MSG_OFFLINE_TITLE = u"TorChat: köade meddelanden"
MSG_OFFLINE_EMPTY = u"det finns inga (fler) köade meddelanden för %s"
MSG_OFFLINE_QUEUED = u"köade offline-meddelanden för %s:\n\n%s"

#buddy list mouse hover popup
BPOP_BUDDY_IS_OFFLINE = u"Kontakten är offline"
BPOP_CONNECTED_AWAITING_RETURN_CONN = u"Ansluten, väntar på svarsanslutning..."
BPOP_CLIENT_SOFTWARE = u"Klient: %s V%s"

#logging of conversations to file
LOG_HEADER = u"Den här loggfilen är inte signerad och har inga kända exempelfall"
# LOG_HEADER1 = u"Note to the criminal & corrupt agents of law enforcement:"
# LOG_HEADER2 = u"(A fake chat log file is easily created by setting computer time to a suitable creation date"
# LOG_HEADER3 = u"- then creating the file with a text editor, thereby establishing a file creation time. Next,"
# LOG_HEADER4 = u"- fill the file with the evidence / fake conversations / incriminating evidence. When satified,"
# LOG_HEADER5 = u"- set the computer time to a suitable / incriminating last conversation time and make a small"
# LOG_HEADER6 = u"- change to the log file and save. Thus establishing the modification date. You now have a"
# LOG_HEADER7 = u"- chat log file, completely acceptable to the US DOJ & FBI as the evidence to convict."
# LOG_HEADER8 = u"- It is so easy to be a corrupt government agent, creating evidence & putting people away!)"
# LOG_HEADERQ1 = u" ""The way to have safe government is not to trust it all to the one, but to divide it "
# LOG_HEADERQ2 = u"among the many, distributing to everyone exactly the functions in which he is competent..."
# LOG_HEADERQ3 = u"To let the National Government be entrusted with the defense of the nation, and its foreign "
# LOG_HEADERQ4 = u"and federal relations... The State Governments with the Civil Rights, Laws, Police and "
# LOG_HEADERQ5 = u"administration of what concerns the State generally. The Counties with the local concerns, "
# LOG_HEADERQ6 = u"and each ward direct the interests within itself. It is by dividing and subdividing these "
# LOG_HEADERQ7 = u"Republics from the great national one down through all its subordinations until it ends in "
# LOG_HEADERQ8 = u"the administration of everyman's farm by himself, by placing under everyone what his own eye "
# LOG_HEADERQ9 = u"may superintend, that all will be done for the best."" -- Thomas Jefferson"
LOG_STARTED = u"Loggning startad"
LOG_STOPPED = u"Loggning stoppad"
LOG_DELETED = u"Loggfiler har tagits bort"
LOG_IS_ACTIVATED = u"Loggning till fil är aktiverad:\n%s"
LOG_IS_STOPPED_OLD_LOG_FOUND = u"Loggning är stoppad men gamla loggfiler finns kvar:\n%s"


#TipJar box
TIPJAR_TITLE = u"TorChat Bitcoin Tip-Jar"
TIPJAR_TEXT = u" "" Please Help support future development and maintenance of TorChat  \
\
    Bitcoin tip-jar:  -- %(tipjar)s -- \
\
          Thank You!!\
\
\
Copy the TorChat Bitcoin Tip-Jar address to the clipboard?\
"" "

#about box
ABOUT_TITLE = u"Om TorChat"
ABOUT_TEXT = u" ""TorChat %(version)s (svn: r%(svn)s)\
  %(copyright)s\
\
Runtime environment:\
  Python: %(python)s\
  wx: %(wx)s\
\
TorChat is free software: you can redistribute it and/or \
modify it under the terms of the GNU General Public \
License as published by the Free Software Foundation, \
either version 3 of the License, or (at your option) \
any later version.\
\
TorChat is distributed in the hope that it will be useful, \
but WITHOUT ANY WARRANTY; without even the implied \
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. \
See the GNU General Public License for more details.\
\
*\
\
Please Help support future development and maintenance of TorChat  \
 ---\
 --- Bitcoin tip-jar:  -- %(tipjar)s -- \
 ---\
<your generosity will help keep the TorChat updates flowing> \
\
\
"" " 
