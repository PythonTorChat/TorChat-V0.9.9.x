# -*- coding: UTF-8 -*-

##############################################################################
#                                                                            #
# Copyright (c) 2007-2010 Bernd Kreuss <prof7bit@gmail.com>                  #
#   Modifications and updates Copyright                                      #
# Copyright (c) 2014-2019  M. Weigand       <doctortor@use.startmail.com>    #
#                                                                            #
# Translation file for TorChat                                               #
#                                                                            #
##############################################################################

LANGUAGE_CODE = u"zh"
LANGUAGE_NAME = u"Chinese" # <-- Please translate, this should be the word "Chinese" in Chinese
LANGUAGE_NAME_ENGLISH = u"Chinese"
TRANSLATOR_NAMES = [u"mickeywaley"]

#buttons
BTN_CANCEL = u"取消"
BTN_OK = u"Ok"             # <-- Please translate
BTN_SAVE_AS = u"另存为..."
BTN_CLOSE = u"关闭"

#status
ST_AVAILABLE = u"可用的"
ST_AWAY = u"离去"
ST_EXTENDED_AWAY = u"扩展的距离"
ST_OFFLINE = u"离线"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = u"显示/隐藏TorChat"
MTB_QUIT = u"退出"

#popup menu
MPOP_CHAT = u"聊天..."
MPOP_SEND_FILE = u"发送文件..."
MPOP_EDIT_CONTACT = u"编辑联络..."
MPOP_DELETE_CONTACT = u"删除联系人..."
MPOP_SHOW_OFFLINE_MESSAGES = u"查看离线消息队列"
MPOP_CLEAR_OFFLINE_MESSAGES = u"清除排队离线消息"
# MPOP_ACTIVATE_LOG = u"Activate logging to file"
# MPOP_STOP_LOG = u"Stop logging"
# MPOP_DELETE_EXISTING_LOG = u"Delete existing log file"
# MPOP_DELETE_AND_STOP_LOG = u"Delete log and stop logging"
MPOP_ADD_CONTACT = u"新增联络人..."
MPOP_ABOUT = u"关于TorChat"
MPOP_TIPJAR = u"TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = u"询问 %s..."
MPOP_SETTINGS = u"设置..."
# MPOP_EDIT_MY_PROFILE = u"Edit my profile..."

#chat window popup menu
CPOP_COPY = u"复制"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = u"确认删除"
D_CONFIRM_DELETE_MESSAGE = u"确实要删除此联络？\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = u"TorChat: 日志记录是积极的"
D_LOG_WARNING_MESSAGE = u"记录到的文件被激活！\n\nLog File: %s\n\n请记住，删除日志文件如果您已经完成调试，因为日志文件可能包含敏感信息。"

#warning about used port
D_WARN_USED_PORT_TITLE = u"TorChat: 端口已在使用中"
D_WARN_USED_PORT_MESSAGE = u"Something, 可能还有TorChat例如，已经在听 %s:%s. 您必须创建一个配置文件使用不同的端口，能够启动TorChat第二次。"

# #warning about unread messages
D_WARN_UNREAD_TITLE = u"TorChat: 未读消息"
D_WARN_UNREAD_MESSAGE = u"有未读消息.\n他们将永远失去！\n\n你真的要退出TorChat呢？"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = u"TorChat: 好友离线"
D_WARN_BUDDY_OFFLINE_MESSAGE = u"此操作是不可能的离线好友"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = u"TorChat: 多个文件"
D_WARN_FILE_ONLY_ONE_MESSAGE = u"您可能无法启动一个操作多个文件传输。开始转让单独或发送一个zip文件，而不是"

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = u"TorChat: 错误保存文件"
D_WARN_FILE_SAVE_ERROR_MESSAGE = u"该文件 '%s' 不能创建.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = u"TorChat: 文件存在"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = u"该文件 '%s' 已存在.\n覆盖它?"

#dialog: add/edit contact
DEC_TITLE_ADD = u"添加新的联系人"
DEC_TITLE_EDIT = u"编辑联络人"
DEC_TORCHAT_ID = u"TorChat ID"
DEC_DISPLAY_NAME = u"显示名称"
DEC_INTRODUCTION = u"导言"
DEC_MSG_16_CHARACTERS = u"该地址必须是16个字符长, 不 %i."
DEC_MSG_ONLY_ALPANUM = u"该地址必须只包含数字和小写字母"
DEC_MSG_ALREADY_ON_LIST = u"%s 已在您的名单"

# #dialog: edit my profile
# DEP_TITLE = u"Edit my profile"
# DEP_NAME = u"Name"
# DEP_TEXT = u"Text"
# DEP_SET_AVATAR = u"Set Avatar"
# DEP_REMOVE_AVATAR = u"Remove Avatar"
# DEP_AVATAR_SELECT_PNG = u"Select .PNG file to use as your avatar (will be scaled to 64*64, may contain transparency)"
# DEP_PNG_FILES = u"PNG files"
# DEP_ALL_FILES = u"All files"
# DEP_WARN_TITLE = u"Avatar selection not possible"
# DEP_WARN_IS_ALREADY = u"This is already the current avatar"
# DEP_WARN_MUST_BE_PNG = u"The avatar must be a .png file"

#file transfer window
DFT_FILE_OPEN_TITLE = u"发送文件 %s"
DFT_FILE_SAVE_TITLE = u"从保存文件 %s"
DFT_SEND = u"发送 %s\nto %s\n%04.1f%% (%i of %i bytes)"
DFT_RECEIVE = u"接收 %s\nfrom %s\n%04.1f%% (%i of %i bytes)"
# DFT_WAITING = u"waiting for connection"
# DFT_STARTING = u"starting transfer"
# DFT_ABORTED = u"transfer aborted"
# DFT_COMPLETE = u"transfer complete"
# DFT_ERROR = u"error"

#settings dialaog
DSET_TITLE = u"TorChat配置"
DSET_NET_TITLE = u"网络"
DSET_NET_ACTIVE = u"活跃"
DSET_NET_INACTIVE = u"无效"
DSET_NET_TOR_ADDRESS = u"Tor的代理地址"
DSET_NET_TOR_SOCKS = u"Socks 端口"
DSET_NET_TOR_CONTROL = u"控制端口"
DSET_NET_OWN_HOSTNAME = u"自己的 TorChat-ID"
DSET_NET_LISTEN_INTERFACE = u"听接口"
DSET_NET_LISTEN_PORT = u"监听端口"
DSET_GUI_TITLE = u"用户界面"
DSET_GUI_LANGUAGE = u"语言"
DSET_GUI_OPEN_MAIN_HIDDEN = u"首先，最小化主窗口"
DSET_GUI_OPEN_CHAT_HIDDEN = u"不要自动打开新窗"
DSET_GUI_NOTIFICATION_POPUP = u"通知弹出"
# DSET_GUI_NOTIFICATION_METHOD = u"Notification method"
DSET_GUI_FLASH_WINDOW = u"闪光的新消息窗口的标题"
DSET_MISC_TITLE = u"临时目录"
DSET_MISC_TEMP_IN_DATA = u"内部数据存储临时文件的目录"
DSET_MISC_TEMP_CUSTOM_DIR = u"临时目录（保留为空操作系统默认）"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = u"轮候时间将邮件发送"
NOTICE_DELAYED_MSG_SENT = u"拖延已发送的邮件"
NOTICE_DELAYED = u"延迟"

#messagebox for offline messages
MSG_OFFLINE_TITLE = u"TorChat：排队的消息"
MSG_OFFLINE_EMPTY = u"没有（更多）排队的消息的 %s"
MSG_OFFLINE_QUEUED = u"排队离线消息 %s:\n\n%s"

# #buddy list mouse hover popup
# BPOP_BUDDY_IS_OFFLINE = u"Buddy is offline"
# BPOP_CONNECTED_AWAITING_RETURN_CONN = u"Connected, awaiting return connection..."
# BPOP_CLIENT_SOFTWARE = u"Client: %s V%s"

# #logging of conversations to file
# LOG_HEADER = u"This log file is not digitally signed and has no cogency of proof of anything."
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
# LOG_STARTED = u"Logging started"
# LOG_STOPPED = u"Logging stopped"
# LOG_DELETED = u"Log files have been deleted"
# LOG_IS_ACTIVATED = u"Logging to file is activated:\n%s"
# LOG_IS_STOPPED_OLD_LOG_FOUND = u"Logging is stopped but old log file still exists:\n%s"


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
ABOUT_TITLE = u"About TorChat"
ABOUT_TEXT = u" ""TorChat %(version)s (build: r%(svn)s)\
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
