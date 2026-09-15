import sys #line:1
import threading #line:2
import subprocess #line:3
import base64 #line:4
import shutil #line:5
import zipfile #line:6
import webbrowser #line:7
import urllib #line:8
import io #line:9
import json #line:10
import os #line:11
import platform #line:12
import time #line:13
from shutil import copyfile #line:14
import re #line:15
import ctypes #line:16
import random #line:17
import ssl #line:18
if sys .version_info [0 ]==3 :#line:20
    import urllib .parse #line:22
    import urllib .request #line:23
    import tkinter as tk #line:24
    from tkinter import filedialog as fd #line:25
    import tkinter .messagebox as tkMessageBox #line:26
    from io import StringIO as StringIO #line:27
    from tkinter import ttk #line:28
else :#line:30
    import Tkinter as tk #line:32
    import tkFileDialog as fd #line:33
    import tkMessageBox #line:34
    from StringIO import StringIO #line:35
    import ttk #line:36
    import urllib2 #line:37
IS_SETTING_WINDOW_OPEN =False #line:40
IS_GLOBAL =True #line:41
IS_PROJECT =False #line:42
IS_PROMOTED =False #line:43
IS_UPDATED =False #line:44
IS_3D_TAB_OPEN =False #line:45
CONST_DEFAULT_GEOMETRY ="458x721"#line:48
CONST_DEFAULT_WINDOW_WIDTH =458 #line:49
CONST_DEFAULT_GEOMETRY_HEIGHT =721 #line:50
CONST_INSTALL_WINDOW_GEOMETRY ="1150x828"#line:52
CONST_INSTALL_WINDOW_WIDTH =1150 #line:53
CONST_INSTALL_GEOMETRY_HEIGHT =828 #line:54
CONST_LOGIN_GEOMETRY =CONST_DEFAULT_GEOMETRY #line:56
CONST_LOGIN_WINDOW_WIDTH =CONST_DEFAULT_WINDOW_WIDTH #line:57
CONST_LOGIN_GEOMETRY_HEIGHT =CONST_DEFAULT_GEOMETRY_HEIGHT #line:58
class Observer :#line:60
    def __init__ (O00OOOO0O0O0O0O00 ,initial_value =0 ):#line:61
        O00OOOO0O0O0O0O00 ._value =initial_value #line:62
        O00OOOO0O0O0O0O00 ._callbacks =[]#line:63
    @property #line:65
    def value (O0OO0OOO00OOOO0O0 ):#line:66
        return O0OO0OOO00OOOO0O0 ._value #line:67
    @value .setter #line:69
    def value (O0000000000O0O0OO ,OO00O00O0O000OO00 ):#line:70
        OOOOO0OOO00O0OO0O =O0000000000O0O0OO ._value #line:71
        O0000000000O0O0OO ._value =OO00O00O0O000OO00 #line:72
        O0000000000O0O0OO ._notify_observers (OOOOO0OOO00O0OO0O ,OO00O00O0O000OO00 )#line:73
    def _notify_observers (O000OOOOOO000OOOO ,O00OO000OO0O00O0O ,OOOOO0OO00O00OOOO ):#line:75
        for OO0O0OO0OO0O0OOOO in O000OOOOOO000OOOO ._callbacks :#line:76
            OO0O0OO0OO0O0OOOO (O00OO000OO0O00O0O ,OOOOO0OO00O00OOOO )#line:77
    def register_callback (OO0OO000O0OOOO000 ,OOO00OOOOOO0OOOOO ):#line:79
        OO0OO000O0OOOO000 ._callbacks .append (OOO00OOOOOO0OOOOO )#line:80
class AfterDownloadView (tk .Frame ):#line:82
    def __init__ (O0OO00OOOO0000OO0 ,O000OOOO000O0OO00 ,flip_table_dir =None ,proj_flip_table_dir =None ,snapeda_library_abs_dir =None ,kicad_mod_filename =None ):#line:83
        O0OO00OOOO0000OO0 .flip_table_dir =flip_table_dir #line:84
        O0OO00OOOO0000OO0 .proj_flip_table_dir =proj_flip_table_dir #line:85
        O0OO00OOOO0000OO0 .snapeda_library_abs_dir =snapeda_library_abs_dir #line:86
        O0OO00OOOO0000OO0 .kicad_mod_filename =kicad_mod_filename #line:87
        O0OO00OOOO0000OO0 .is_download_complete =O000OOOO000O0OO00 .is_download_complete #line:88
        O0OO00OOOO0000OO0 .is_help_me_window =O000OOOO000O0OO00 .is_help_me_window #line:89
        O0OO00OOOO0000OO0 .parent =tk .Toplevel ()#line:90
        O0OOOO000OO000OO0 =int ((O000OOOO000O0OO00 .winfo_screenwidth ()/2 )-(458 /2 ))+(O000OOOO000O0OO00 .winfo_x ()/2 )#line:91
        O0000O0OO0000OOO0 =int ((O000OOOO000O0OO00 .winfo_screenheight ()/2 )-(275 /2 ))+(O000OOOO000O0OO00 .winfo_y ()/2 )#line:92
        O0OO00OOOO0000OO0 .parent .geometry ('%dx%d+%d+%d'%(458 ,275 ,O0OOOO000OO000OO0 ,O0000O0OO0000OOO0 ))#line:93
        O0OO00OOOO0000OO0 .parent .grab_set ()#line:94
        global IS_SETTING_WINDOW_OPEN #line:95
        IS_SETTING_WINDOW_OPEN =True #line:96
        O0OO00OOOO0000OO0 .parent .resizable (False ,False )#line:97
        O0OO00OOOO0000OO0 .parent .minsize (width =458 ,height =275 )#line:98
        O0OO00OOOO0000OO0 .is_windows =(os .name =='nt')#line:99
        O0OO00OOOO0000OO0 .dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:100
        if O0OO00OOOO0000OO0 .is_windows :#line:101
            O0OO00OOOO0000OO0 .windata_dir =os .path .join (os .getenv ('HOMEDRIVE'),os .getenv ('HOMEPATH'),"SnapEDA Kicad Plugin")#line:104
            O0OO00OOOO0000OO0 .appdata_dir =os .path .join (O0OO00OOOO0000OO0 .windata_dir ,"App")#line:105
        else :#line:106
            O0OO00OOOO0000OO0 .appdata_dir =os .path .join (O0OO00OOOO0000OO0 .dir_path ,"assets")#line:107
        O0OO00OOOO0000OO0 .powered_image_dir =os .path .join (O0OO00OOOO0000OO0 .appdata_dir ,"orb6glbv.png")#line:109
        O0OO00OOOO0000OO0 .icon_bitmap_dir =os .path .join (O0OO00OOOO0000OO0 .appdata_dir ,"32x32.ico")#line:110
        O0OO00OOOO0000OO0 .info_label_img_dir =os .path .join (O0OO00OOOO0000OO0 .appdata_dir ,'info_button.png')#line:111
        O0OO00OOOO0000OO0 .folder_label_img_dir =os .path .join (O0OO00OOOO0000OO0 .appdata_dir ,'folder_label.png')#line:112
        O0OO00OOOO0000OO0 .save_button_img_dir =os .path .join (O0OO00OOOO0000OO0 .appdata_dir ,'save_button.png')#line:113
        if O0OO00OOOO0000OO0 .is_windows :#line:114
            O0OO00OOOO0000OO0 .parent .iconbitmap (O0OO00OOOO0000OO0 .icon_bitmap_dir )#line:115
        O0OO00OOOO0000OO0 .initialize_user_interface ()#line:116
        O0OO00OOOO0000OO0 .parent .protocol ("WM_DELETE_WINDOW",lambda :O0OO00OOOO0000OO0 .on_closing (O000OOOO000O0OO00 ))#line:118
    def on_closing (OO0OO0O00OOOOO0OO ,OO00O0O0000O0OOOO ):#line:120
        OO00O00OOOOO0OOO0 =os .path .join (OO0OO0O00OOOOO0OO .appdata_dir ,"info.json")#line:122
        with open (OO00O00OOOOO0OOO0 )as OOOO0O0OOOO00OOOO :#line:123
            O000O000O000O0000 =json .load (OOOO0O0OOOO00OOOO )#line:124
        if OO0OO0O00OOOOO0OO .flip_table_dir is not None or OO0OO0O00OOOOO0OO .proj_flip_table_dir is not None or OO0OO0O00OOOOO0OO .snapeda_library_abs_dir is not None :#line:126
            try :#line:128
                if O000O000O000O0000 ['setting_autoplace_footprint']:#line:129
                    OOO0OOO0O00O0O0O0 =pcbnew .GetBoard ()#line:130
                    O0000O0O0OO0OOOOO =pcbnew .FootprintLoad (OO0OO0O00OOOOO0OO .snapeda_library_abs_dir ,OO0OO0O00OOOOO0OO .kicad_mod_filename )#line:131
                    OOO0OOO0O00O0O0O0 .Add (O0000O0O0OO0OOOOO )#line:132
                    wx .CallAfter (pcbnew .Refresh )#line:133
            except :#line:134
                OOO0OOO0O00O0O0O0 =pcbnew .GetBoard ()#line:135
                O0000O0O0OO0OOOOO =pcbnew .FootprintLoad (OO0OO0O00OOOOO0OO .snapeda_library_abs_dir ,OO0OO0O00OOOOO0OO .kicad_mod_filename )#line:136
                OOO0OOO0O00O0O0O0 .Add (O0000O0O0OO0OOOOO )#line:137
                wx .CallAfter (pcbnew .Refresh )#line:138
            global IS_GLOBAL #line:141
            global IS_PROJECT #line:142
            if (IS_GLOBAL is False )and (IS_PROJECT is False ):#line:145
                IS_GLOBAL =True #line:146
            if IS_GLOBAL :#line:148
                with open (OO0OO0O00OOOOO0OO .flip_table_dir ,"r+")as OOOO00OOOO000O000 :#line:149
                    O00OO0OO0O0O000OO =OOOO00OOOO000O000 .read ()#line:150
                    if ("(lib (name \""+O000O000O000O0000 ['kicad_library_name']+"\")(type KiCad)(uri \""+OO0OO0O00OOOOO0OO .snapeda_library_abs_dir +"\")")not in O00OO0OO0O0O000OO :#line:151
                        OO000000O00OO0OO0 =('  (lib (name "'+O000O000O000O0000 ['kicad_library_name']+'")(type KiCad)(uri "'+OO0OO0O00OOOOO0OO .snapeda_library_abs_dir +'")(options "")(descr ""))')+"\n\n)"#line:152
                        OO000000O00OO0OO0 =OO000000O00OO0OO0 .replace ("'","")#line:153
                        OO0OO0O0OOOO0O0OO =O00OO0OO0O0O000OO [:-2 ]+OO000000O00OO0OO0 #line:154
                        OOOO00OOOO000O000 .seek (0 )#line:155
                        OOOO00OOOO000O000 .write (OO0OO0O0OOOO0O0OO )#line:156
                        OOOO00OOOO000O000 .truncate ()#line:157
            if IS_PROJECT :#line:159
                with open (OO0OO0O00OOOOO0OO .proj_flip_table_dir ,"r+")as OOOO00OOOO000O000 :#line:160
                    O00OO0OO0O0O000OO =OOOO00OOOO000O000 .read ()#line:161
                    if ("(lib (name \""+O000O000O000O0000 ['kicad_library_name']+"\")(type KiCad)(uri \""+OO0OO0O00OOOOO0OO .snapeda_library_abs_dir +"\")")not in O00OO0OO0O0O000OO :#line:162
                        OO000000O00OO0OO0 =('  (lib (name "'+O000O000O000O0000 ['kicad_library_name']+'")(type KiCad)(uri "'+OO0OO0O00OOOOO0OO .snapeda_library_abs_dir +'")(options "")(descr ""))')+"\n\n)"#line:163
                        OO000000O00OO0OO0 =OO000000O00OO0OO0 .replace ("'","")#line:164
                        OO0OO0O0OOOO0O0OO =O00OO0OO0O0O000OO [:-2 ]+OO000000O00OO0OO0 #line:165
                        OOOO00OOOO000O000 .seek (0 )#line:166
                        OOOO00OOOO000O000 .write (OO0OO0O0OOOO0O0OO )#line:167
                        OOOO00OOOO000O000 .truncate ()#line:168
        print ('aferdownloadview closed')#line:170
        global IS_SETTING_WINDOW_OPEN #line:171
        IS_SETTING_WINDOW_OPEN =False #line:172
        OO0OO0O00OOOOO0OO .parent .destroy ()#line:173
    def resize (OO00OOO000000O000 ,O0000O00OO0000000 ,O000OO0O00O00O0O0 ,OO0000O00OOO00O00 ):#line:175
        ""#line:179
        if sys .version_info [0 ]==3 :#line:180
            O0OO000OO0OO000O0 =O0000O00OO0000000 .width ()#line:181
            OOOO0OO0O0O0O0OO0 =O0000O00OO0000000 .height ()#line:182
            O000OOOO000OO0O00 =max (O0OO000OO0OO000O0 ,OOOO0OO0O0O0O0OO0 )#line:183
            O000OOO0OO0OO0000 =max (O000OO0O00O00O0O0 ,OO0000O00OOO00O00 )#line:184
            if O000OOOO000OO0O00 >O000OOO0OO0OO0000 :#line:185
                return O0000O00OO0000000 .subsample (int (O000OOOO000OO0O00 /O000OOO0OO0OO0000 ))#line:186
            else :#line:187
                return O0000O00OO0000000 .zoom (int (O000OOO0OO0OO0000 /O000OOOO000OO0O00 ))#line:188
        else :#line:189
            O0OO000OO0OO000O0 =O0000O00OO0000000 .width ()#line:190
            OOOO0OO0O0O0O0OO0 =O0000O00OO0000000 .height ()#line:191
            O000OOOO000OO0O00 =max (O0OO000OO0OO000O0 ,OOOO0OO0O0O0O0OO0 )#line:192
            O000OOO0OO0OO0000 =max (O000OO0O00O00O0O0 ,OO0000O00OOO00O00 )#line:193
            if O000OOOO000OO0O00 >O000OOO0OO0OO0000 :#line:194
                return O0000O00OO0000000 .subsample (O000OOOO000OO0O00 /O000OOO0OO0OO0000 )#line:195
            else :#line:196
                return O0000O00OO0000000 .zoom (O000OOO0OO0OO0000 /O000OOOO000OO0O00 )#line:197
    def save_settings_callback (OOO0OOOOOOOO0OOOO ,O0O00O0OOOO00OOO0 ):#line:199
        print ('info closed')#line:200
        global IS_SETTING_WINDOW_OPEN #line:201
        IS_SETTING_WINDOW_OPEN =False #line:202
        OOO0OOOOOOOO0OOOO .parent .destroy ()#line:203
    def open_folder_callback (OO0O0000OOO00OOOO ,O00OOO00O00OOOOOO ):#line:205
        print ('Opening directory: '+OO0O0000OOO00OOOO .open_dir )#line:206
        open (OO0O0000OOO00OOOO .open_dir ,"r+")#line:207
    def global_checkbox_callback (O0OOO0OOO00000000 ,O00OO0O0OOOOO0OOO ):#line:209
        global IS_GLOBAL #line:210
        if O0OOO0OOO00000000 .global_var .get ()==0 :#line:211
            IS_GLOBAL =True #line:212
        else :#line:213
            IS_GLOBAL =False #line:214
    def project_checkbox_callback (OO00OOOOOO00OOOO0 ,O000OO0O0000OO000 ):#line:217
        global IS_PROJECT #line:218
        if OO00OOOOOO00OOOO0 .project_var .get ()==0 :#line:219
            IS_PROJECT =True #line:220
        else :#line:221
            IS_PROJECT =False #line:222
    def initialize_user_interface (OO00O00000O0OO000 ):#line:225
        OO00O00000O0OO000 .parent .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:226
        OO00O00000O0OO000 .parent .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:227
        OO00O00000O0OO000 .parent_container =tk .Frame (OO00O00000O0OO000 .parent ,bg ="white")#line:228
        OO00O00000O0OO000 .parent_container .grid (row =0 ,column =0 ,sticky ="NEWS")#line:229
        OO00O00000O0OO000 .parent_container .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:230
        OO00O00000O0OO000 .parent_container .grid_rowconfigure (0 ,weight =1 )#line:231
        OO00O00000O0OO000 .main_frame =tk .Frame (OO00O00000O0OO000 .parent_container ,bg ="white")#line:232
        OO00O00000O0OO000 .main_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:233
        for O0000OOOO00000OOO in range (5 ):#line:234
            OO00O00000O0OO000 .main_frame .grid_rowconfigure (O0000OOOO00000OOO ,weight =1 ,uniform ="foo")#line:235
        OO00O00000O0OO000 .main_frame .grid (row =0 ,column =0 ,sticky ="NEWS")#line:236
        OO000OOO0O0O0OO0O ="Done"#line:238
        if OO00O00000O0OO000 .is_download_complete is False :#line:239
            OO000OOO0O0O0OO0O ="No models available."#line:240
            OO00O00000O0OO000 .done_button =tk .Label (OO00O00000O0OO000 .main_frame ,cursor ="hand2",bg ="#FF761A",fg ="white",text =OO000OOO0O0O0OO0O ,font =("Open Sans",13 ,"bold"))#line:241
            OO00O00000O0OO000 .done_button .grid (row =4 ,column =0 ,sticky ="NEWS")#line:242
            OO00O00000O0OO000 .done_button .bind ('<Button-1>',OO00O00000O0OO000 .on_closing )#line:243
            return #line:244
        if OO00O00000O0OO000 .flip_table_dir is not None or OO00O00000O0OO000 .proj_flip_table_dir is not None or OO00O00000O0OO000 .snapeda_library_abs_dir is not None :#line:246
            OO00000O00OOOOOO0 =os .path .join (OO00O00000O0OO000 .appdata_dir ,"info.json")#line:248
            with open (OO00000O00OOOOOO0 )as OOOO0OOOOO00OO00O :#line:249
                OO0OO00OOO0O00O00 =json .load (OOOO0OOOOO00OO00O )#line:250
            OO00O00000O0OO000 .open_dir =OO0OO00OOO0O00O00 ['kicad_library_dir']#line:251
            if len (OO00O00000O0OO000 .open_dir )>48 :#line:252
                OO00O00000O0OO000 .open_dir ='...'+OO00O00000O0OO000 .open_dir [len (OO00O00000O0OO000 .open_dir )-45 :]#line:253
            OO00O00000O0OO000 .folder_container =tk .Frame (OO00O00000O0OO000 .main_frame ,bg ="white")#line:255
            OO00O00000O0OO000 .folder_container .grid_columnconfigure (0 ,weight =2 ,uniform ="foo")#line:256
            OO00O00000O0OO000 .folder_container .grid_columnconfigure (1 ,weight =6 ,uniform ="foo")#line:257
            OO00O00000O0OO000 .folder_container .grid_rowconfigure (1 ,weight =1 ,uniform ="foo")#line:258
            OO00O00000O0OO000 .folder_container .grid (row =1 ,column =0 ,sticky ="NEWS")#line:259
            OO00O00000O0OO000 .folder_label_img =tk .PhotoImage (file =OO00O00000O0OO000 .folder_label_img_dir )#line:260
            OO00O00000O0OO000 .folder_label =tk .Label (OO00O00000O0OO000 .folder_container ,bg ="white",image =OO00O00000O0OO000 .folder_label_img )#line:261
            OO00O00000O0OO000 .folder_label .grid (row =0 ,column =0 ,sticky ="NEWS")#line:262
            OO00O00000O0OO000 .folder_input_label =tk .Label (OO00O00000O0OO000 .folder_container ,bg ="white",text =OO00O00000O0OO000 .open_dir )#line:263
            OO00O00000O0OO000 .folder_input_label .grid (row =0 ,column =1 ,sticky ="NWS",padx =(0 ,15 ))#line:264
        OO00O00000O0OO000 .checkbox_frame =tk .Frame (OO00O00000O0OO000 .main_frame ,bg ="white")#line:268
        OO00O00000O0OO000 .checkbox_frame .grid (row =2 ,column =0 ,sticky ="NEWS")#line:269
        OO00O00000O0OO000 .checkbox_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:270
        for O0000OOOO00000OOO in range (2 ):#line:271
            OO00O00000O0OO000 .checkbox_frame .grid_columnconfigure (O0000OOOO00000OOO ,weight =1 ,uniform ="foo")#line:272
        OO00O00000O0OO000 .global_var =tk .IntVar ()#line:273
        OO00O00000O0OO000 .global_checkbox =tk .Checkbutton (OO00O00000O0OO000 .checkbox_frame ,variable =OO00O00000O0OO000 .global_var ,bg ="white",fg ="#FF761A",text ="Global",borderwidth =0 ,highlightthickness =0 )#line:274
        OO00O00000O0OO000 .global_checkbox .grid (row =0 ,column =0 ,sticky ="NES",padx =(0 ,20 ))#line:275
        OO00O00000O0OO000 .project_var =tk .IntVar ()#line:276
        OO00O00000O0OO000 .project_checkbox =tk .Checkbutton (OO00O00000O0OO000 .checkbox_frame ,variable =OO00O00000O0OO000 .project_var ,bg ="white",fg ="#FF761A",text ="Project Specific",borderwidth =0 ,highlightthickness =0 )#line:277
        OO00O00000O0OO000 .project_checkbox .grid (row =0 ,column =1 ,sticky ="NWS",padx =(20 ,0 ))#line:278
        global IS_GLOBAL #line:279
        global IS_PROJECT #line:280
        if IS_GLOBAL :#line:281
            OO00O00000O0OO000 .global_checkbox .select ()#line:282
        else :#line:283
            OO00O00000O0OO000 .global_checkbox .deselect ()#line:284
        if IS_PROJECT :#line:285
            OO00O00000O0OO000 .project_checkbox .select ()#line:286
        else :#line:287
            OO00O00000O0OO000 .project_checkbox .deselect ()#line:288
        OO00O00000O0OO000 .global_checkbox .bind ('<Button-1>',OO00O00000O0OO000 .global_checkbox_callback )#line:289
        OO00O00000O0OO000 .project_checkbox .bind ('<Button-1>',OO00O00000O0OO000 .project_checkbox_callback )#line:290
        try :#line:292
            if OO0OO00OOO0O00O00 ['setting_autoplace_footprint']:#line:293
                tk .Label (OO00O00000O0OO000 .main_frame ,bg ="white",text ="Note: Autoplacement feature is on.\nYou should see the footprint on the board after download.").grid (row =3 ,column =0 ,sticky ="NEW")#line:294
        except :#line:295
            tk .Label (OO00O00000O0OO000 .main_frame ,bg ="white",text ="Note: Autoplacement feature is on.\nYou should see the footprint on the board after download.").grid (row =3 ,column =0 ,sticky ="NEW")#line:296
        OO00O00000O0OO000 .footer_frame =tk .Frame (OO00O00000O0OO000 .main_frame ,bg ="white")#line:299
        OO00O00000O0OO000 .footer_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:300
        OO00O00000O0OO000 .footer_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:301
        OO00O00000O0OO000 .footer_frame .grid (row =4 ,column =0 ,sticky ="NEWS")#line:302
        OO00O00000O0OO000 .save_button_img =tk .PhotoImage (file =OO00O00000O0OO000 .save_button_img_dir )#line:303
        OO00O00000O0OO000 .save_button =tk .Label (OO00O00000O0OO000 .footer_frame ,cursor ="hand2",image =OO00O00000O0OO000 .save_button_img )#line:304
        OO00O00000O0OO000 .save_button .grid (row =0 ,column =0 ,sticky ="ES",padx =(0 ,25 ),pady =(0 ,25 ))#line:305
        OO00O00000O0OO000 .save_button .bind ('<Button-1>',OO00O00000O0OO000 .on_closing )#line:306
class InfoView (tk .Frame ):#line:309
    def __init__ (OO0000000000O0OO0 ,OO0O0OO0O0O0O000O ):#line:310
        OO0000000000O0OO0 .is_help_me_window =OO0O0OO0O0O0O000O .is_help_me_window #line:311
        OO0000000000O0OO0 .parent =tk .Toplevel ()#line:312
        O00O00O0OOOO0O000 =int ((OO0O0OO0O0O0O000O .winfo_screenwidth ()/2 )-(393 /2 ))+(OO0O0OO0O0O0O000O .winfo_x ()/2 )#line:313
        O0O000O000000O0OO =int ((OO0O0OO0O0O0O000O .winfo_screenheight ()/2 )-(495 /2 ))+(OO0O0OO0O0O0O000O .winfo_y ()/2 )#line:314
        OO0000000000O0OO0 .parent .geometry ('%dx%d+%d+%d'%(393 ,495 ,O00O00O0OOOO0O000 ,O0O000O000000O0OO ))#line:315
        OO0000000000O0OO0 .parent .wait_visibility ()#line:316
        OO0000000000O0OO0 .parent .grab_set ()#line:317
        global IS_SETTING_WINDOW_OPEN #line:318
        IS_SETTING_WINDOW_OPEN =True #line:319
        OO0000000000O0OO0 .parent .resizable (False ,False )#line:320
        OO0000000000O0OO0 .parent .minsize (width =393 ,height =495 )#line:321
        OO0000000000O0OO0 .is_windows =(os .name =='nt')#line:322
        OO0000000000O0OO0 .dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:323
        if OO0000000000O0OO0 .is_windows :#line:324
            OO0000000000O0OO0 .windata_dir =os .path .join (os .getenv ('HOMEDRIVE'),os .getenv ('HOMEPATH'),"SnapEDA Kicad Plugin")#line:327
            OO0000000000O0OO0 .appdata_dir =os .path .join (OO0000000000O0OO0 .windata_dir ,"App")#line:328
        else :#line:329
            OO0000000000O0OO0 .appdata_dir =os .path .join (OO0000000000O0OO0 .dir_path ,"assets")#line:330
        OO0000000000O0OO0 .powered_image_dir =os .path .join (OO0000000000O0OO0 .appdata_dir ,"orb6glbv.png")#line:332
        OO0000000000O0OO0 .icon_bitmap_dir =os .path .join (OO0000000000O0OO0 .appdata_dir ,"32x32.ico")#line:333
        OO0000000000O0OO0 .info_placeholder_img_dir =os .path .join (OO0000000000O0OO0 .appdata_dir ,'info_placeholder.png')#line:334
        OO0000000000O0OO0 .info_label_img_dir =os .path .join (OO0000000000O0OO0 .appdata_dir ,'info_button.png')#line:335
        OO0000000000O0OO0 .talk_to_us_button_image_dir =os .path .join (OO0000000000O0OO0 .appdata_dir ,'talk_to_us_button.png')#line:336
        if OO0000000000O0OO0 .is_windows :#line:338
            OO0000000000O0OO0 .parent .iconbitmap (OO0000000000O0OO0 .icon_bitmap_dir )#line:339
        OO0000000000O0OO0 .initialize_user_interface ()#line:340
        OO0000000000O0OO0 .parent .protocol ("WM_DELETE_WINDOW",lambda :OO0000000000O0OO0 .on_closing (OO0O0OO0O0O0O000O ))#line:342
    def on_closing (O0OO00OO0O00O0000 ,OOO0000O00O0O0O0O ):#line:344
        print ('closed info')#line:345
        global IS_SETTING_WINDOW_OPEN #line:346
        IS_SETTING_WINDOW_OPEN =False #line:347
        O0OO00OO0O00O0000 .parent .destroy ()#line:348
    def resize (O0O00OOOO00O0OOOO ,O0OOO00OO0OO0O000 ,O00O0OOO00OO0OOO0 ,OO0O0OO00OOOOO0OO ):#line:350
        ""#line:354
        if sys .version_info [0 ]==3 :#line:355
            OOO0OOO00O0O00O00 =O0OOO00OO0OO0O000 .width ()#line:356
            O0O0000OOOOOOO0OO =O0OOO00OO0OO0O000 .height ()#line:357
            O0OO00OO00000OO0O =max (OOO0OOO00O0O00O00 ,O0O0000OOOOOOO0OO )#line:358
            OOO0000O0O000O0OO =max (O00O0OOO00OO0OOO0 ,OO0O0OO00OOOOO0OO )#line:359
            if O0OO00OO00000OO0O >OOO0000O0O000O0OO :#line:360
                return O0OOO00OO0OO0O000 .subsample (int (O0OO00OO00000OO0O /OOO0000O0O000O0OO ))#line:361
            else :#line:362
                return O0OOO00OO0OO0O000 .zoom (int (OOO0000O0O000O0OO /O0OO00OO00000OO0O ))#line:363
        else :#line:364
            OOO0OOO00O0O00O00 =O0OOO00OO0OO0O000 .width ()#line:365
            O0O0000OOOOOOO0OO =O0OOO00OO0OO0O000 .height ()#line:366
            O0OO00OO00000OO0O =max (OOO0OOO00O0O00O00 ,O0O0000OOOOOOO0OO )#line:367
            OOO0000O0O000O0OO =max (O00O0OOO00OO0OOO0 ,OO0O0OO00OOOOO0OO )#line:368
            if O0OO00OO00000OO0O >OOO0000O0O000O0OO :#line:369
                return O0OOO00OO0OO0O000 .subsample (O0OO00OO00000OO0O /OOO0000O0O000O0OO )#line:370
            else :#line:371
                return O0OOO00OO0OO0O000 .zoom (OOO0000O0O000O0OO /O0OO00OO00000OO0O )#line:372
    def save_settings_callback (O0O00000OO0O0000O ,O0O0O00000OOO00O0 ):#line:374
        print ('info closed')#line:375
        global IS_SETTING_WINDOW_OPEN #line:376
        IS_SETTING_WINDOW_OPEN =False #line:377
        O0O00000OO0O0000O .parent .destroy ()#line:378
    def talk_to_us_button_callback (OO000OOOOOOO00O00 ,O000OO00O00O000OO ):#line:380
        webbrowser .open ('mailto:?to=info@snapeda.com',new =1 )#line:381
    def initialize_user_interface (OO000O00O0OO0OO00 ):#line:383
        OO000O00O0OO0OO00 .parent .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:384
        OO000O00O0OO0OO00 .parent .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:385
        OO000O00O0OO0OO00 .parent_container =tk .Frame (OO000O00O0OO0OO00 .parent ,bg ="white")#line:386
        OO000O00O0OO0OO00 .parent_container .grid (row =0 ,column =0 ,sticky ="NEWS")#line:387
        OO000O00O0OO0OO00 .parent_container .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:388
        OO000O00O0OO0OO00 .parent_container .grid_rowconfigure (0 ,weight =1 )#line:389
        OO000O00O0OO0OO00 .main_frame =tk .Frame (OO000O00O0OO0OO00 .parent_container ,bg ="white")#line:390
        OO000O00O0OO0OO00 .main_frame .grid (row =0 ,column =0 ,columnspan =1 ,sticky ="NEWS")#line:391
        OO000O00O0OO0OO00 .main_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:393
        for O0O000O00O00000OO in range (20 ):#line:394
            OO000O00O0OO0OO00 .main_frame .grid_rowconfigure (O0O000O00O00000OO ,weight =1 ,uniform ="foo")#line:395
        OO000O00O0OO0OO00 .navbar_frame =tk .Frame (OO000O00O0OO0OO00 .main_frame ,bg ="white")#line:398
        OO000O00O0OO0OO00 .navbar_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:399
        OO000O00O0OO0OO00 .navbar_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:400
        OO000O00O0OO0OO00 .navbar_frame .grid (row =0 ,column =0 ,rowspan =2 ,sticky ="NEWS")#line:401
        OO000O00O0OO0OO00 .info_label_img =tk .PhotoImage (file =OO000O00O0OO0OO00 .info_label_img_dir )#line:402
        OO000O00O0OO0OO00 .setting_label =tk .Label (OO000O00O0OO0OO00 .navbar_frame ,bg ="white",fg ="#FF761B",image =OO000O00O0OO0OO00 .info_label_img )#line:403
        OO000O00O0OO0OO00 .setting_label .grid (row =0 ,column =0 ,sticky ="W",padx =(20 ,0 ))#line:404
        OO000O00O0OO0OO00 .info_frame =tk .Frame (OO000O00O0OO0OO00 .main_frame ,bg ="white")#line:407
        OO000O00O0OO0OO00 .info_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:408
        OO000O00O0OO0OO00 .info_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:409
        OO000O00O0OO0OO00 .info_frame .grid (row =3 ,column =0 ,rowspan =14 ,sticky ="NEWS")#line:410
        OO000O00O0OO0OO00 .info_placeholder_img =tk .PhotoImage (file =OO000O00O0OO0OO00 .info_placeholder_img_dir )#line:411
        OO000O00O0OO0OO00 .info_placeholder =tk .Label (OO000O00O0OO0OO00 .info_frame ,bg ="white",image =OO000O00O0OO0OO00 .info_placeholder_img )#line:412
        OO000O00O0OO0OO00 .info_placeholder .grid (row =0 ,column =0 ,sticky ="NEWS")#line:413
        OOOO000O000O00OO0 ='1. Search for the part\n\n2. Click on Download\n\n3. Go to Place > Footprint or >  Symbol\n\n4. Find the part in your "SnapEDA Library"\n\n5. Use it in your design\n'#line:415
        if (OO000O00O0OO0OO00 .is_help_me_window is True ):#line:416
            OOOO000O000O00OO0 ='For any concerns or suggestions in using\nthis plugin, kindly contact us at\ninfo@snapeda.com.'#line:417
        OO000O00O0OO0OO00 .instruction_label =tk .Label (OO000O00O0OO0OO00 .info_placeholder ,justify =tk .LEFT ,bg ="#E5E5E5",fg ="#304E70",text =OOOO000O000O00OO0 ,font =("Open Sans",10 ))#line:418
        OO000O00O0OO0OO00 .instruction_label .grid (row =0 ,column =0 ,sticky ="NWS",padx =(30 ,0 ),pady =(80 ,0 ))#line:419
        OO000O00O0OO0OO00 .footer_frame =tk .Frame (OO000O00O0OO0OO00 .main_frame ,bg ="white")#line:422
        OO000O00O0OO0OO00 .footer_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:423
        OO000O00O0OO0OO00 .footer_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:424
        OO000O00O0OO0OO00 .footer_frame .grid (row =18 ,column =0 ,rowspan =2 ,columnspan =2 ,sticky ="NEWS")#line:425
        OO000O00O0OO0OO00 .talk_to_us_button_image =tk .PhotoImage (file =OO000O00O0OO0OO00 .talk_to_us_button_image_dir )#line:426
        OO000O00O0OO0OO00 .talk_to_us_button =tk .Label (OO000O00O0OO0OO00 .footer_frame ,bg ="white",cursor ="hand2",image =OO000O00O0OO0OO00 .talk_to_us_button_image )#line:427
        OO000O00O0OO0OO00 .talk_to_us_button .grid (row =0 ,column =0 ,sticky ="E",padx =(0 ,25 ),pady =(0 ,10 ))#line:428
        OO000O00O0OO0OO00 .talk_to_us_button .bind ('<Button-1>',OO000O00O0OO0OO00 .talk_to_us_button_callback )#line:429
class SettingsView (tk .Frame ):#line:431
    def __init__ (O0O00OOOOOOOOOO00 ,OO0000O0O00O000OO ):#line:432
        O0O00OOOOOOOOOO00 .parent =tk .Toplevel ()#line:433
        O00O0OOOO00OO00O0 =int ((OO0000O0O00O000OO .winfo_screenwidth ()/2 )-(458 /2 ))+(OO0000O0O00O000OO .winfo_x ()/2 )#line:434
        O000OO0OOO0OO0OO0 =int ((OO0000O0O00O000OO .winfo_screenheight ()/2 )-(600 /2 ))+(OO0000O0O00O000OO .winfo_y ()/2 )#line:435
        O0O00OOOOOOOOOO00 .parent .geometry ('%dx%d+%d+%d'%(458 ,600 ,O00O0OOOO00OO00O0 ,O000OO0OOO0OO0OO0 ))#line:436
        O0O00OOOOOOOOOO00 .parent .wait_visibility ()#line:437
        O0O00OOOOOOOOOO00 .parent .grab_set ()#line:438
        global IS_SETTING_WINDOW_OPEN #line:439
        IS_SETTING_WINDOW_OPEN =True #line:440
        O0O00OOOOOOOOOO00 .parent .resizable (False ,False )#line:441
        O0O00OOOOOOOOOO00 .parent .minsize (width =458 ,height =600 )#line:442
        O0O00OOOOOOOOOO00 .is_windows =(os .name =='nt')#line:443
        O0O00OOOOOOOOOO00 .dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:444
        if O0O00OOOOOOOOOO00 .is_windows :#line:445
            O0O00OOOOOOOOOO00 .windata_dir =os .path .join (os .getenv ('HOMEDRIVE'),os .getenv ('HOMEPATH'),"SnapEDA Kicad Plugin")#line:448
            O0O00OOOOOOOOOO00 .appdata_dir =os .path .join (O0O00OOOOOOOOOO00 .windata_dir ,"App")#line:449
            O0O00OOOOOOOOOO00 .flip_table_dir =os .path .join (os .getenv ('APPDATA'),'kicad','fp-lib-table')#line:452
        else :#line:453
            O0O00OOOOOOOOOO00 .appdata_dir =os .path .join (O0O00OOOOOOOOOO00 .dir_path ,"assets")#line:454
            O0O00OOOOOOOOOO00 .flip_table_dir =os .path .join (os .path .expanduser ("~"),'.config','kicad','fp-lib-table')#line:458
        O0O00OOOOOOOOOO00 .powered_image_dir =os .path .join (O0O00OOOOOOOOOO00 .appdata_dir ,"orb6glbv.png")#line:460
        O0O00OOOOOOOOOO00 .icon_bitmap_dir =os .path .join (O0O00OOOOOOOOOO00 .appdata_dir ,"32x32.ico")#line:461
        O0O00OOOOOOOOOO00 .settings_label_img_dir =os .path .join (O0O00OOOOOOOOOO00 .appdata_dir ,'settings_button.png')#line:462
        O0O00OOOOOOOOOO00 .setting_placeholder_img_dir =os .path .join (O0O00OOOOOOOOOO00 .appdata_dir ,'settings_placeholder.png')#line:463
        O0O00OOOOOOOOOO00 .settings_input_placeholder_dir =os .path .join (O0O00OOOOOOOOOO00 .appdata_dir ,'settings_input_placeholder.png')#line:464
        O0O00OOOOOOOOOO00 .save_button_img_dir =os .path .join (O0O00OOOOOOOOOO00 .appdata_dir ,'save_button.png')#line:465
        if O0O00OOOOOOOOOO00 .is_windows :#line:467
            O0O00OOOOOOOOOO00 .parent .iconbitmap (O0O00OOOOOOOOOO00 .icon_bitmap_dir )#line:468
        O0O00OOOOOOOOOO00 .initialize_user_interface ()#line:469
        O0O00OOOOOOOOOO00 .parent .protocol ("WM_DELETE_WINDOW",lambda :O0O00OOOOOOOOOO00 .on_closing (OO0000O0O00O000OO ))#line:471
    def on_closing (OOOO0O00O00000OO0 ,O0OOO000000OO0000 ):#line:473
        print ('closed settings')#line:474
        global IS_SETTING_WINDOW_OPEN #line:475
        IS_SETTING_WINDOW_OPEN =False #line:476
        OOOO0O00O00000OO0 .parent .destroy ()#line:477
    def resize (OO00OO00000O0O000 ,OOOOO0OO00OO0O000 ,OO000OO00O0O000OO ,O00OOOO00O0OO0OO0 ):#line:479
        ""#line:483
        if sys .version_info [0 ]==3 :#line:484
            O00O000OOOOO00OOO =OOOOO0OO00OO0O000 .width ()#line:485
            O000OO0OO000OO00O =OOOOO0OO00OO0O000 .height ()#line:486
            O0O0OOOO0OOOOOO00 =max (O00O000OOOOO00OOO ,O000OO0OO000OO00O )#line:487
            OOO0OO0O0O0000O0O =max (OO000OO00O0O000OO ,O00OOOO00O0OO0OO0 )#line:488
            if O0O0OOOO0OOOOOO00 >OOO0OO0O0O0000O0O :#line:489
                return OOOOO0OO00OO0O000 .subsample (int (O0O0OOOO0OOOOOO00 /OOO0OO0O0O0000O0O ))#line:490
            else :#line:491
                return OOOOO0OO00OO0O000 .zoom (int (OOO0OO0O0O0000O0O /O0O0OOOO0OOOOOO00 ))#line:492
        else :#line:493
            O00O000OOOOO00OOO =OOOOO0OO00OO0O000 .width ()#line:494
            O000OO0OO000OO00O =OOOOO0OO00OO0O000 .height ()#line:495
            O0O0OOOO0OOOOOO00 =max (O00O000OOOOO00OOO ,O000OO0OO000OO00O )#line:496
            OOO0OO0O0O0000O0O =max (OO000OO00O0O000OO ,O00OOOO00O0OO0OO0 )#line:497
            if O0O0OOOO0OOOOOO00 >OOO0OO0O0O0000O0O :#line:498
                return OOOOO0OO00OO0O000 .subsample (O0O0OOOO0OOOOOO00 /OOO0OO0O0O0000O0O )#line:499
            else :#line:500
                return OOOOO0OO00OO0O000 .zoom (OOO0OO0O0O0000O0O /O0O0OOOO0OOOOOO00 )#line:501
    def save_settings_callback (OOO00O0OOOO0O00O0 ,OOOOO000OOO0OO00O ):#line:503
        OO00O0OO0O00000OO =os .path .join (OOO00O0OOOO0O00O0 .appdata_dir ,"info.json")#line:504
        with open (OO00O0OO0O00000OO )as OOO0OOO0OO0O0O0O0 :#line:505
            OO0O0O0O0OOOOOO00 =json .load (OOO0OOO0OO0O0O0O0 )#line:506
        OOOOO0O0O0O00OOO0 =False #line:509
        with open (OOO00O0OOOO0O00O0 .flip_table_dir ,"r+")as O00O0000O0OOO00O0 :#line:510
            O0O0O000O0O0O0O00 =O00O0000O0OOO00O0 .read ()#line:511
            O0O0O0000OO0O0000 ="(lib (name \""+OOO00O0OOOO0O00O0 .kicad_dir_name_entry .get ()#line:512
            if O0O0O0000OO0O0000 in O0O0O000O0O0O0O00 :#line:513
                O0O0O0000OO0O0000 =("(lib (name \""+OOO00O0OOOO0O00O0 .kicad_dir_name_entry .get ()+"\")(type KiCad)(uri \""+os .path .join (OOO00O0OOOO0O00O0 .selected_dir ,OOO00O0OOOO0O00O0 .kicad_dir_name_entry .get ())+'.pretty\"')#line:514
                print (O0O0O0000OO0O0000 )#line:515
                if O0O0O0000OO0O0000 not in O0O0O000O0O0O0O00 :#line:516
                    print ('invalid')#line:517
                    OOOOO0O0O0O00OOO0 =True #line:518
                    O00O0000O0OOO00O0 .close ()#line:519
                else :#line:520
                    print ('valid')#line:521
        if (OOOOO0O0O0O00OOO0 ):#line:523
            tkMessageBox .showwarning ("Warning","Duplicate library name.\n Please choose a different lib name.")#line:524
            return #line:525
        if OOO00O0OOOO0O00O0 .auto_place_value .get ()==0 :#line:527
            OO0O0O0O0OOOOOO00 ['setting_autoplace_footprint']=False #line:528
        else :#line:529
            OO0O0O0O0OOOOOO00 ['setting_autoplace_footprint']=True #line:530
        OO0O0O0O0OOOOOO00 ['kicad_library_dir']=OOO00O0OOOO0O00O0 .selected_dir #line:532
        OO0O0O0O0OOOOOO00 ['kicad_library_name']=OOO00O0OOOO0O00O0 .kicad_dir_name_entry .get ()#line:533
        with open (OO00O0OO0O00000OO ,'w')as OO00OO0OO0OOO0OOO :#line:534
            json .dump (OO0O0O0O0OOOOOO00 ,OO00OO0OO0OOO0OOO )#line:535
        print ('Settings saved: '+OOO00O0OOOO0O00O0 .selected_dir +', lib name: '+OOO00O0OOOO0O00O0 .kicad_dir_name_entry .get ())#line:536
        global IS_SETTING_WINDOW_OPEN #line:537
        IS_SETTING_WINDOW_OPEN =False #line:538
        OOO00O0OOOO0O00O0 .parent .destroy ()#line:539
    def file_input_callback (OO0000000OOO000O0 ,O0OO0OOO0OO0000OO ):#line:541
        O00O0OO000OO0O0OO =os .path .expanduser (os .path .join (OO0000000OOO000O0 .selected_dir ,''))#line:542
        OO0000000OOO000O0 .selected_dir =fd .askdirectory (initialdir =O00O0OO000OO0O0OO ).replace ('/','\\')#line:543
        if (OO0000000OOO000O0 .selected_dir is None )or (OO0000000OOO000O0 .selected_dir ==''):#line:544
            OO0000000OOO000O0 .selected_dir =str (O00O0OO000OO0O0OO )#line:545
        if len (OO0000000OOO000O0 .selected_dir )>35 :#line:546
            OO0000000OOO000O0 .download_dir .set ('...'+OO0000000OOO000O0 .selected_dir [len (OO0000000OOO000O0 .selected_dir )-33 :])#line:547
        else :#line:548
            OO0000000OOO000O0 .download_dir .set (OO0000000OOO000O0 .selected_dir )#line:549
        print (OO0000000OOO000O0 .selected_dir )#line:550
    def initialize_user_interface (OOO0OO000O0O000O0 ):#line:552
        OOO0OO000O0O000O0 .parent .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:553
        OOO0OO000O0O000O0 .parent .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:554
        OOO0OO000O0O000O0 .parent_container =tk .Frame (OOO0OO000O0O000O0 .parent ,bg ="white")#line:555
        OOO0OO000O0O000O0 .parent_container .grid (row =0 ,column =0 ,sticky ="NEWS")#line:556
        OOO0OO000O0O000O0 .parent_container .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:557
        OOO0OO000O0O000O0 .parent_container .grid_rowconfigure (0 ,weight =1 )#line:558
        OOO0OO000O0O000O0 .main_frame =tk .Frame (OOO0OO000O0O000O0 .parent_container ,bg ="white")#line:559
        OOO0OO000O0O000O0 .main_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:560
        OOO0OO000O0O000O0 .main_frame .grid_rowconfigure (0 ,weight =3 ,uniform ="foo")#line:561
        OOO0OO000O0O000O0 .main_frame .grid_rowconfigure (1 ,weight =5 ,uniform ="foo")#line:562
        OOO0OO000O0O000O0 .main_frame .grid_rowconfigure (2 ,weight =5 ,uniform ="foo")#line:563
        OOO0OO000O0O000O0 .main_frame .grid_rowconfigure (3 ,weight =3 ,uniform ="foo")#line:564
        OOO0OO000O0O000O0 .main_frame .grid (row =0 ,column =0 ,columnspan =1 ,sticky ="NEWS")#line:565
        OOO0OO000O0O000O0 .navbar_frame =tk .Frame (OOO0OO000O0O000O0 .main_frame ,bg ="white")#line:569
        OOO0OO000O0O000O0 .navbar_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:570
        OOO0OO000O0O000O0 .navbar_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:571
        OOO0OO000O0O000O0 .navbar_frame .grid (row =0 ,column =0 ,sticky ="NEWS")#line:572
        OOO0OO000O0O000O0 .settings_label_img =tk .PhotoImage (file =OOO0OO000O0O000O0 .settings_label_img_dir )#line:573
        OOO0OO000O0O000O0 .setting_label =tk .Label (OOO0OO000O0O000O0 .navbar_frame ,bg ="white",fg ="#FF761B",image =OOO0OO000O0O000O0 .settings_label_img )#line:574
        OOO0OO000O0O000O0 .setting_label .grid (row =0 ,column =0 ,sticky ="W",padx =(25 ,0 ))#line:575
        OOO0OO000O0O000O0 .body_frame =tk .Frame (OOO0OO000O0O000O0 .main_frame ,bg ="white")#line:578
        OOO0OO000O0O000O0 .body_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:579
        OOO0OO000O0O000O0 .body_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:580
        OOO0OO000O0O000O0 .body_frame .grid (row =1 ,column =0 ,sticky ="NEWS")#line:581
        OOO0OO000O0O000O0 .setting_placeholder_img =tk .PhotoImage (file =OOO0OO000O0O000O0 .setting_placeholder_img_dir )#line:582
        OOO0OO000O0O000O0 .setting_001_placeholder =tk .Label (OOO0OO000O0O000O0 .body_frame ,bg ="white",image =OOO0OO000O0O000O0 .setting_placeholder_img )#line:583
        OOO0OO000O0O000O0 .setting_001_placeholder .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:584
        OOO0OO000O0O000O0 .setting_001_placeholder .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:585
        OOO0OO000O0O000O0 .setting_001_placeholder .grid_rowconfigure (1 ,weight =3 ,uniform ="foo")#line:586
        OOO0OO000O0O000O0 .setting_001_placeholder .grid_rowconfigure (2 ,weight =3 ,uniform ="foo")#line:587
        OOO0OO000O0O000O0 .setting_001_placeholder .grid_rowconfigure (3 ,weight =1 ,uniform ="foo")#line:588
        OOO0OO000O0O000O0 .setting_001_placeholder .grid (row =0 ,column =0 ,sticky ="NEWS")#line:589
        OOO0OO000O0O000O0 .form_top =tk .Frame (OOO0OO000O0O000O0 .setting_001_placeholder ,bg ="#E5E5E5")#line:591
        OOO0OO000O0O000O0 .form_top .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:592
        OOO0OO000O0O000O0 .form_top .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:593
        OOO0OO000O0O000O0 .form_top .grid_columnconfigure (1 ,weight =2 ,uniform ="foo")#line:594
        OOO0OO000O0O000O0 .form_top .grid (row =1 ,column =0 ,sticky ="NEWS",padx =(30 ,30 ),pady =(1 ,0 ))#line:595
        OOO0OO000O0O000O0 .settings_input_placeholder =tk .PhotoImage (file =OOO0OO000O0O000O0 .settings_input_placeholder_dir )#line:598
        O00O0OOOO0OOO0OOO =os .path .join (OOO0OO000O0O000O0 .appdata_dir ,"info.json")#line:599
        with open (O00O0OOOO0OOO0OOO )as O0OOOOOO00O0OOOO0 :#line:600
            O00000O0OOOOO0O00 =json .load (O0OOOOOO00O0OOOO0 )#line:601
        tk .Label (OOO0OO000O0O000O0 .form_top ,bg ="#E5E5E5",fg ="#666460",text ="Libraries Path",font =("Open Sans",11 ,"bold")).grid (row =0 ,column =0 ,sticky ="NEWS")#line:603
        tk .Label (OOO0OO000O0O000O0 .form_top ,bg ="#E5E5E5",image =OOO0OO000O0O000O0 .settings_input_placeholder ,cursor ="hand2").grid (row =0 ,column =1 ,sticky ="NEWS")#line:604
        O0OO0000OO0000O0O =O00000O0OOOOO0O00 ['kicad_library_dir']#line:605
        OOO0OO000O0O000O0 .selected_dir =O0OO0000OO0000O0O #line:606
        if len (O0OO0000OO0000O0O )>35 :#line:607
            O0OO0000OO0000O0O ='...'+O0OO0000OO0000O0O [len (O0OO0000OO0000O0O )-33 :]#line:608
        OOO0OO000O0O000O0 .download_dir =tk .StringVar ()#line:609
        OOO0OO000O0O000O0 .download_dir .set (O0OO0000OO0000O0O )#line:610
        OOO0OO000O0O000O0 .file_input =tk .Label (OOO0OO000O0O000O0 .form_top ,bg ="white",textvariable =OOO0OO000O0O000O0 .download_dir ,cursor ="hand2",font =("Open Sans",8 ))#line:611
        OOO0OO000O0O000O0 .file_input .grid (row =0 ,column =1 ,sticky ="NEWS",padx =(20 ,20 ),pady =(20 ,20 ))#line:612
        OOO0OO000O0O000O0 .file_input .bind ('<Button-1>',OOO0OO000O0O000O0 .file_input_callback )#line:613
        OOO0OO000O0O000O0 .form_bottom =tk .Frame (OOO0OO000O0O000O0 .setting_001_placeholder ,bg ="#E5E5E5")#line:616
        OOO0OO000O0O000O0 .form_bottom .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:617
        OOO0OO000O0O000O0 .form_bottom .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:618
        OOO0OO000O0O000O0 .form_bottom .grid_columnconfigure (1 ,weight =2 ,uniform ="foo")#line:619
        OOO0OO000O0O000O0 .form_bottom .grid (row =2 ,column =0 ,sticky ="NEWS",padx =(30 ,30 ),pady =(0 ,1 ))#line:620
        tk .Label (OOO0OO000O0O000O0 .form_bottom ,bg ="#E5E5E5",fg ="#666460",text ="Library Name",font =("Open Sans",11 ,"bold")).grid (row =0 ,column =0 ,sticky ="NEWS")#line:622
        tk .Label (OOO0OO000O0O000O0 .form_bottom ,bg ="#E5E5E5",image =OOO0OO000O0O000O0 .settings_input_placeholder ,cursor ="hand2").grid (row =0 ,column =1 ,sticky ="NEWS")#line:623
        OOO0OO000O0O000O0 .entry_value =tk .StringVar ()#line:624
        OOO0OO000O0O000O0 .entry_value .set (O00000O0OOOOO0O00 ['kicad_library_name'])#line:625
        OOO0OO000O0O000O0 .kicad_dir_name_entry =tk .Entry (OOO0OO000O0O000O0 .form_bottom ,textvariable =OOO0OO000O0O000O0 .entry_value ,bg ="white",font =("Open Sans",8 ),borderwidth =0 ,highlightthickness =0 )#line:626
        OOO0OO000O0O000O0 .kicad_dir_name_entry .grid (row =0 ,column =1 ,sticky ="NEWS",padx =(20 ,20 ),pady =(20 ,20 ))#line:627
        OOO0OO000O0O000O0 .body_auto_place_frame =tk .Frame (OOO0OO000O0O000O0 .main_frame ,bg ="white")#line:630
        OOO0OO000O0O000O0 .body_auto_place_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:631
        OOO0OO000O0O000O0 .body_auto_place_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:632
        OOO0OO000O0O000O0 .body_auto_place_frame .grid (row =2 ,column =0 ,sticky ="NEW")#line:633
        OOO0OO000O0O000O0 .auto_place_value =tk .IntVar ()#line:634
        OOO0OO000O0O000O0 .auto_place_checkbox =tk .Checkbutton (OOO0OO000O0O000O0 .body_auto_place_frame ,variable =OOO0OO000O0O000O0 .auto_place_value ,fg ="#FF761A",bg ="white",text ="Auto place footprints",borderwidth =0 ,highlightthickness =0 )#line:635
        try :#line:636
            if O00000O0OOOOO0O00 ['setting_autoplace_footprint']:#line:637
                OOO0OO000O0O000O0 .auto_place_checkbox .select ()#line:638
            else :#line:639
                OOO0OO000O0O000O0 .auto_place_checkbox .deselect ()#line:640
        except :#line:641
            OOO0OO000O0O000O0 .auto_place_checkbox .select ()#line:642
        OOO0OO000O0O000O0 .auto_place_checkbox .grid (row =0 ,column =0 ,sticky ="NEW")#line:643
        OOO0OO000O0O000O0 .footer_frame =tk .Frame (OOO0OO000O0O000O0 .main_frame ,bg ="white")#line:646
        OOO0OO000O0O000O0 .footer_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:647
        OOO0OO000O0O000O0 .footer_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:648
        OOO0OO000O0O000O0 .footer_frame .grid (row =3 ,column =0 ,sticky ="NEWS")#line:649
        OOO0OO000O0O000O0 .save_button_img =tk .PhotoImage (file =OOO0OO000O0O000O0 .save_button_img_dir )#line:650
        OOO0OO000O0O000O0 .save_button =tk .Label (OOO0OO000O0O000O0 .footer_frame ,cursor ="hand2",image =OOO0OO000O0O000O0 .save_button_img )#line:651
        OOO0OO000O0O000O0 .save_button .grid (row =0 ,column =0 ,sticky ="ES",padx =(0 ,25 ),pady =(0 ,25 ))#line:652
        OOO0OO000O0O000O0 .save_button .bind ('<Button-1>',OOO0OO000O0O000O0 .save_settings_callback )#line:653
class TableView (tk .Frame ):#line:655
    ""#line:658
    def __init__ (OO00OO0OOOOO00O00 ,O0000O000O00O00OO ):#line:660
        tk .Frame .__init__ (OO00OO0OOOOO00O00 ,O0000O000O00O00OO )#line:661
        OO00OO0OOOOO00O00 .parent =O0000O000O00O00OO #line:662
        OO00OO0OOOOO00O00 .dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:663
        OO00OO0OOOOO00O00 .is_mac =platform .mac_ver ()[0 ]!=""#line:664
        OO00OO0OOOOO00O00 .is_windows =(os .name =='nt')#line:665
        if OO00OO0OOOOO00O00 .is_windows :#line:666
            OO00OO0OOOOO00O00 .windata_dir =os .path .join (os .getenv ('HOMEDRIVE'),os .getenv ('HOMEPATH'),"SnapEDA Kicad Plugin")#line:669
            OO00OO0OOOOO00O00 .flip_table_dir =os .path .join (os .getenv ('APPDATA'),'kicad','fp-lib-table')#line:672
            OO00OO0OOOOO00O00 .proj_flip_table_dir =os .path .join (os .getenv ('APPDATA'),'kicad','prj-fp-lib-table')#line:675
            if not os .path .exists (OO00OO0OOOOO00O00 .proj_flip_table_dir ):#line:677
                OO0O0O0O000OOOO00 ='(fp_lib_table\n\n)'#line:678
                with open (OO00OO0OOOOO00O00 .proj_flip_table_dir ,'w')as O00O00O0OOOOO0OOO :#line:679
                    O00O00O0OOOOO0OOO .write (OO0O0O0O000OOOO00 )#line:680
                    O00O00O0OOOOO0OOO .close #line:681
            OO00OO0OOOOO00O00 .appdata_dir =os .path .join (OO00OO0OOOOO00O00 .windata_dir ,"App")#line:683
            if not os .path .exists (OO00OO0OOOOO00O00 .windata_dir ):#line:685
                os .makedirs (OO00OO0OOOOO00O00 .windata_dir )#line:686
            if not os .path .exists (OO00OO0OOOOO00O00 .appdata_dir ):#line:687
                os .makedirs (OO00OO0OOOOO00O00 .appdata_dir )#line:688
            OO00OO0OOOOO00O00 .kicad_library_dir =os .path .join (OO00OO0OOOOO00O00 .windata_dir ,'KiCad Library')#line:690
            OO00OO0OOOOO00O00 .snapeda_library_abs_dir =os .path .join (OO00OO0OOOOO00O00 .kicad_library_dir ,'SnapEDA Library.pretty')#line:692
            OO00OO0OOOOO00O00 .snapeda_threedee_models_dir =os .path .join (OO00OO0OOOOO00O00 .kicad_library_dir ,'SnapEDA 3D Models')#line:694
            if not os .path .exists (OO00OO0OOOOO00O00 .kicad_library_dir ):#line:696
                os .makedirs (OO00OO0OOOOO00O00 .kicad_library_dir )#line:697
            if not os .path .exists (OO00OO0OOOOO00O00 .snapeda_library_abs_dir ):#line:698
                os .makedirs (OO00OO0OOOOO00O00 .snapeda_library_abs_dir )#line:699
            if not os .path .exists (OO00OO0OOOOO00O00 .snapeda_threedee_models_dir ):#line:700
                os .makedirs (OO00OO0OOOOO00O00 .snapeda_threedee_models_dir )#line:701
        elif OO00OO0OOOOO00O00 .is_mac :#line:702
            OO00OO0OOOOO00O00 .macdata_dir =os .path .join (os .path .expanduser ("~"),"Documents","SnapEDA Kicad Plugin")#line:703
            OO00OO0OOOOO00O00 .appdata_dir =os .path .join (OO00OO0OOOOO00O00 .macdata_dir ,"App")#line:704
            OO00OO0OOOOO00O00 .flip_table_dir =os .path .join (os .getenv ('HOME'),'library','preferences','kicad','fp-lib-table')#line:705
            OO00OO0OOOOO00O00 .proj_flip_table_dir =os .path .join (os .getenv ('HOME'),'library','preferences','kicad','prj-fp-lib-table')#line:706
            OO00OO0OOOOO00O00 .kicad_common_dir =os .path .join (os .getenv ('HOME'),'library','preferences','kicad','kicad_common')#line:707
            OO00OO0OOOOO00O00 .kicad_library_dir =os .path .join (OO00OO0OOOOO00O00 .macdata_dir ,'KiCad Library')#line:708
            OO00OO0OOOOO00O00 .snapeda_library_dir =os .path .join (OO00OO0OOOOO00O00 .kicad_library_dir ,'SnapEDA Library')#line:710
            OO00OO0OOOOO00O00 .snapeda_library_abs_dir =os .path .join (OO00OO0OOOOO00O00 .kicad_library_dir ,'SnapEDA Library.pretty')#line:712
            OO00OO0OOOOO00O00 .snapeda_threedee_models_dir =os .path .join (OO00OO0OOOOO00O00 .kicad_library_dir ,'SnapEDA 3D Models')#line:714
            if not os .path .exists (OO00OO0OOOOO00O00 .appdata_dir ):#line:715
                os .makedirs (OO00OO0OOOOO00O00 .appdata_dir )#line:716
            if not os .path .exists (OO00OO0OOOOO00O00 .kicad_library_dir ):#line:717
                os .makedirs (OO00OO0OOOOO00O00 .kicad_library_dir )#line:718
            if not os .path .exists (OO00OO0OOOOO00O00 .snapeda_library_dir ):#line:719
                os .makedirs (OO00OO0OOOOO00O00 .snapeda_library_dir )#line:720
            if not os .path .exists (OO00OO0OOOOO00O00 .snapeda_library_abs_dir ):#line:721
                os .makedirs (OO00OO0OOOOO00O00 .snapeda_library_abs_dir )#line:722
            if not os .path .exists (OO00OO0OOOOO00O00 .snapeda_threedee_models_dir ):#line:723
                os .makedirs (OO00OO0OOOOO00O00 .snapeda_threedee_models_dir )#line:724
            if not os .path .exists (OO00OO0OOOOO00O00 .proj_flip_table_dir ):#line:726
                OO0O0O0O000OOOO00 ='(fp_lib_table\n\n)'#line:727
                with open (OO00OO0OOOOO00O00 .proj_flip_table_dir ,'w')as O00O00O0OOOOO0OOO :#line:728
                    O00O00O0OOOOO0OOO .write (OO0O0O0O000OOOO00 )#line:729
                    O00O00O0OOOOO0OOO .close #line:730
        else :#line:731
            OO00OO0OOOOO00O00 .appdata_dir =os .path .join (OO00OO0OOOOO00O00 .dir_path ,"assets")#line:732
            if not os .path .exists (OO00OO0OOOOO00O00 .appdata_dir ):#line:733
                os .makedirs (OO00OO0OOOOO00O00 .appdata_dir )#line:734
            OO00OO0OOOOO00O00 .flip_table_dir =os .path .join (os .path .expanduser ("~"),'.config','kicad','fp-lib-table')#line:738
            OO00OO0OOOOO00O00 .proj_flip_table_dir =os .path .join (os .path .expanduser ("~"),'.config','kicad','prj-fp-lib-table')#line:743
            if not os .path .exists (OO00OO0OOOOO00O00 .proj_flip_table_dir ):#line:745
                OO0O0O0O000OOOO00 ='(fp_lib_table\n\n)'#line:746
                with open (OO00OO0OOOOO00O00 .proj_flip_table_dir ,'w')as O00O00O0OOOOO0OOO :#line:747
                    O00O00O0OOOOO0OOO .write (OO0O0O0O000OOOO00 )#line:748
                    O00O00O0OOOOO0OOO .close #line:749
            O0OO0O0OOO0O000OO =os .path .expanduser ("~")#line:751
            OO00OO0OOOOO00O00 .kicad_library_dir =os .path .join (O0OO0O0OOO0O000OO ,'KiCad Library')#line:752
            OO00OO0OOOOO00O00 .snapeda_library_abs_dir =os .path .join (OO00OO0OOOOO00O00 .kicad_library_dir ,'SnapEDA Library.pretty')#line:754
            OO00OO0OOOOO00O00 .snapeda_threedee_models_dir =os .path .join (OO00OO0OOOOO00O00 .kicad_library_dir ,'SnapEDA 3D Models')#line:756
            if not os .path .exists (OO00OO0OOOOO00O00 .kicad_library_dir ):#line:757
                os .makedirs (OO00OO0OOOOO00O00 .kicad_library_dir )#line:758
            if not os .path .exists (OO00OO0OOOOO00O00 .snapeda_library_abs_dir ):#line:759
                os .makedirs (OO00OO0OOOOO00O00 .snapeda_library_abs_dir )#line:760
            if not os .path .exists (OO00OO0OOOOO00O00 .snapeda_threedee_models_dir ):#line:761
                os .makedirs (OO00OO0OOOOO00O00 .snapeda_threedee_models_dir )#line:762
        OO00OO0OOOOO00O00 .icon_bitmap_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"32x32.ico")#line:764
        OO00OO0OOOOO00O00 .filter_button_image_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"neeo2s8g.png")#line:765
        OO00OO0OOOOO00O00 .settings_button_image_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"7svfoe57.png")#line:766
        OO00OO0OOOOO00O00 .about_button_image_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"2kdtezsl.png")#line:767
        OO00OO0OOOOO00O00 .passive_components_image_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"t3gwhnzh.png")#line:768
        OO00OO0OOOOO00O00 .all_button_image_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"dsyrvfl9.png")#line:769
        OO00OO0OOOOO00O00 .powered_image_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"orb6glbv.png")#line:770
        OO00OO0OOOOO00O00 .datasheet_button_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"oxfarxz8.png")#line:771
        OO00OO0OOOOO00O00 .datasheet_available_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"m4lamm2w.png")#line:772
        OO00OO0OOOOO00O00 .datasheet_not_available_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"4cnn9kkf.png")#line:773
        OO00OO0OOOOO00O00 .symbol_available_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"huaxvbtm.png")#line:774
        OO00OO0OOOOO00O00 .symbol_not_available_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"tmuhgmxh.png")#line:775
        OO00OO0OOOOO00O00 .footprint_available_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"3ruuehki.png")#line:776
        OO00OO0OOOOO00O00 .footprint_not_available_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"62r7iuz7.png")#line:777
        OO00OO0OOOOO00O00 .available_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"uku4ceuv.png")#line:778
        OO00OO0OOOOO00O00 .not_available_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"zah3n8r4.png")#line:779
        OO00OO0OOOOO00O00 .prev_bg_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"iu2ma3jp.png")#line:780
        OO00OO0OOOOO00O00 .next_bg_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"witafnjf.png")#line:781
        OO00OO0OOOOO00O00 .selected_page_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"izif2qd8.png")#line:782
        OO00OO0OOOOO00O00 .download_button_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"download+orange.png")#line:783
        OO00OO0OOOOO00O00 .view_button_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"viewonsnapeda+white.png")#line:784
        OO00OO0OOOOO00O00 .search_button_image_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"4i2efbui.png")#line:785
        OO00OO0OOOOO00O00 .loading_image_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"jwhk6qck.gif")#line:786
        OO00OO0OOOOO00O00 .avatar_image_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"avatar1.png")#line:787
        OO00OO0OOOOO00O00 .settings_menu_img =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'home_menu.png')#line:788
        OO00OO0OOOOO00O00 .home_menu_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'home_menu.png')#line:789
        OO00OO0OOOOO00O00 .how_it_works_menu_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'how_it_works_menu.png')#line:790
        OO00OO0OOOOO00O00 .info_menu_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'info_menu.png')#line:791
        OO00OO0OOOOO00O00 .logout_menu_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'logout_menu.png')#line:792
        OO00OO0OOOOO00O00 .settings_menu_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'settings_menu.png')#line:793
        OO00OO0OOOOO00O00 .not_available_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'not_available.png')#line:794
        OO00OO0OOOOO00O00 .request_now_button_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'request_now_button.png')#line:795
        OO00OO0OOOOO00O00 .threedee_model_not_available_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"3d_model_not_available_img.png")#line:796
        OO00OO0OOOOO00O00 .threedee_available_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"threedee_model_available.png")#line:797
        OO00OO0OOOOO00O00 .threedee_unavailable_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,"threedee_model_unavailable.png")#line:798
        if IS_UPDATED :#line:800
            OO00OO0OOOOO00O00 .update_menu_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'update_menu.png')#line:801
        else :#line:802
            OO00OO0OOOOO00O00 .update_menu_img_dir =os .path .join (OO00OO0OOOOO00O00 .appdata_dir ,'notif_update_menu+(2).png')#line:803
        OO00OO0OOOOO00O00 .initialize_user_interface ()#line:805
    def download_component (OO000000O000O00O0 ,OO0000O0O0O0O0000 ):#line:807
        global IS_PROMOTED #line:809
        if bool (random .getrandbits (1 ))and not IS_PROMOTED :#line:810
            IS_PROMOTED =True #line:811
            O00O000O00OO0OO00 =os .path .join (OO000000O000O00O0 .appdata_dir ,"info.json")#line:813
            print (OO000000O000O00O0 .appdata_dir )#line:814
            with open (O00O000O00OO0OO00 )as O0O0O000O0OO000OO :#line:815
                OOOO0O00OO0O0000O =json .load (O0O0O000O0OO000OO )#line:816
            webbrowser .open ("https://delighted.com/t/JxbeJK7q?name={}".format (OOOO0O00OO0O0000O .get ('username','')),new =2 )#line:817
        if not OO000000O000O00O0 .is_downloading :#line:818
            OO000000O000O00O0 .is_downloading =True #line:819
            O00O0O00OOO00OO0O =threading .Thread (target =OO000000O000O00O0 .download_data )#line:820
            O00O0O00OOO00OO0O .start ()#line:821
            OO000000O000O00O0 .download_button .config (state ="disabled")#line:822
    def download_data (OOOO00OO0OOO00OO0 ):#line:825
        global IS_SETTING_WINDOW_OPEN #line:826
        OOOO00OO0OOO00OO0 .parent .is_download_complete =True #line:827
        OO0OOO00O0O00OOO0 =""#line:829
        O0OOOOO0O0OO000OO =os .path .dirname (os .path .realpath (__file__ ))#line:830
        if OOOO00OO0OOO00OO0 .is_windows or OOOO00OO0OOO00OO0 .is_mac :#line:832
            with open (os .path .join (OOOO00OO0OOO00OO0 .appdata_dir ,".token"),"r")as O0OO0O0000OO00O0O :#line:833
                OO0OOO00O0O00OOO0 =str (O0OO0O0000OO00O0O .readline ())#line:834
        else :#line:835
            with open (os .path .join (O0OOOOO0O0OO000OO ,".token"),"r")as O0OO0O0000OO00O0O :#line:836
                OO0OOO00O0O00OOO0 =str (O0OO0O0000OO00O0O .readline ())#line:837
        O000OO0O00O0OO000 ="https://www.snapeda.com/api/v1/parts/download_part"#line:838
        OO00OOO000O000O00 ={'User-Agent':"Kicad"}#line:839
        O0OOO00OO000O0OO0 ={'part_number':str (OOOO00OO0OOO00OO0 .part_number ),'manufacturer':str (OOOO00OO0OOO00OO0 .manufacturer ),'has_symbol':OOOO00OO0OOO00OO0 .has_symbol ,'has_footprint':OOOO00OO0OOO00OO0 .has_footprint ,'uniqueid':OOOO00OO0OOO00OO0 .uniqueid ,'token':OO0OOO00O0O00OOO0 ,'format':"kicad_mod",'ref':"kicad-plugin",'plugin':'kicad'}#line:850
        try :#line:852
            if sys .version_info [0 ]==3 :#line:853
                OO0OOOOOO0O0OO00O =urllib .parse .urlencode (O0OOO00OO000O0OO0 ).encode ("utf-8")#line:854
                OO0OOO0000O0O00O0 =urllib .request .Request (O000OO0O00O0OO000 ,OO0OOOOOO0O0OO00O ,headers =OO00OOO000O000O00 )#line:855
                OOOOOO0OOO0O0O0OO =urllib .request .urlopen (OO0OOO0000O0O00O0 ).read ()#line:856
            else :#line:857
                OO0OOOOOO0O0OO00O =urllib .urlencode (O0OOO00OO000O0OO0 )#line:858
                OO0OOO0000O0O00O0 =urllib2 .Request (O000OO0O00O0OO000 ,OO0OOOOOO0O0OO00O ,headers =OO00OOO000O000O00 )#line:859
                OOOOOO0OOO0O0O0OO =urllib2 .urlopen (OO0OOO0000O0O00O0 ).read ()#line:860
        except :#line:861
            OOOO00OO0OOO00OO0 .download_button .config (state ="normal",text ="Download")#line:863
            OOOO00OO0OOO00OO0 .is_downloading =False #line:864
            OOOO00OO0OOO00OO0 .parent .is_download_complete =False #line:865
            if IS_SETTING_WINDOW_OPEN is False :#line:866
                OOOO00OO0OOO00OO0 .parent .is_help_me_window =False #line:867
                AfterDownloadView (OOOO00OO0OOO00OO0 .parent )#line:868
            return #line:869
        OOOO00OO0OOO00OO0 .download_url =json .loads (OOOOOO0OOO0O0O0OO )["url"]#line:870
        print (OOOO00OO0OOO00OO0 .download_url )#line:871
        OO00OOO000O000O00 ={'User-Agent':"Kicad"}#line:872
        if len (OOOO00OO0OOO00OO0 .download_url )==0 :#line:873
            OOOO00OO0OOO00OO0 .download_button .config (state ="normal",text ="Download")#line:875
            OOOO00OO0OOO00OO0 .is_downloading =False #line:876
            OOOO00OO0OOO00OO0 .parent .is_download_complete =False #line:877
            if IS_SETTING_WINDOW_OPEN is False :#line:878
                OOOO00OO0OOO00OO0 .parent .is_help_me_window =False #line:879
                AfterDownloadView (OOOO00OO0OOO00OO0 .parent )#line:880
            return #line:881
        OOOO00OO0OOO00OO0 .part_number =OOOO00OO0OOO00OO0 .part_number .replace ('/','_')#line:882
        if sys .version_info [0 ]==3 :#line:883
            O00OOO0O00OO0O0OO =urllib .request .Request (OOOO00OO0OOO00OO0 .download_url ,headers =OO00OOO000O000O00 )#line:884
            O0OO00O0O0OO0O0O0 =urllib .request .urlopen (O00OOO0O00OO0O0OO )#line:885
        else :#line:886
            O00OOO0O00OO0O0OO =urllib2 .Request (OOOO00OO0OOO00OO0 .download_url ,headers =OO00OOO000O000O00 )#line:887
            O0OO00O0O0OO0O0O0 =urllib2 .urlopen (O00OOO0O00OO0O0OO )#line:888
        O00OO0O00000OOOO0 =os .path .join (OOOO00OO0OOO00OO0 .appdata_dir ,"info.json")#line:890
        OO0OOOOOO0O0OO00O ={}#line:891
        with open (O00OO0O00000OOOO0 )as OO0000000O0OOO0OO :#line:892
            OO0OOOOOO0O0OO00O =json .load (OO0000000O0OOO0OO )#line:893
        OOOO00OO0OOO00OO0 .kicad_library_dir =OO0OOOOOO0O0OO00O ['kicad_library_dir']#line:895
        OOOO00OO0OOO00OO0 .snapeda_library_dir =os .path .join (OOOO00OO0OOO00OO0 .kicad_library_dir ,OO0OOOOOO0O0OO00O ['kicad_library_name'])#line:896
        OOOO00OO0OOO00OO0 .snapeda_library_abs_dir =os .path .join (OOOO00OO0OOO00OO0 .kicad_library_dir ,OO0OOOOOO0O0OO00O ['kicad_library_name']+'.pretty')#line:897
        OOOO00000OOOOO00O =os .path .join (OOOO00OO0OOO00OO0 .kicad_library_dir ,'temp')#line:898
        OO00OO00O00O0OOO0 =os .path .join (OOOO00000OOOOO00O ,str (OOOO00OO0OOO00OO0 .part_number ))#line:899
        if not os .path .exists (OOOO00OO0OOO00OO0 .kicad_library_dir ):#line:900
            os .makedirs (OOOO00OO0OOO00OO0 .kicad_library_dir )#line:901
        if not os .path .exists (OOOO00OO0OOO00OO0 .snapeda_library_dir ):#line:902
            os .makedirs (OOOO00OO0OOO00OO0 .snapeda_library_dir )#line:903
        if not os .path .exists (OO00OO00O00O0OOO0 ):#line:904
            os .makedirs (OO00OO00O00O0OOO0 )#line:905
        if not os .path .exists (OOOO00OO0OOO00OO0 .snapeda_library_abs_dir ):#line:906
            os .makedirs (OOOO00OO0OOO00OO0 .snapeda_library_abs_dir )#line:907
        with open (os .path .join (OO00OO00O00O0OOO0 ,OOOO00OO0OOO00OO0 .part_number +".zip"),"wb")as O0OO0O0000OO00O0O :#line:908
            shutil .copyfileobj (O0OO00O0O0OO0O0O0 ,O0OO0O0000OO00O0O )#line:909
        with zipfile .ZipFile (os .path .join (OO00OO00O00O0OOO0 ,OOOO00OO0OOO00OO0 .part_number +".zip"))as O00OO0O0O0O0O0000 :#line:911
            O00OO0O0O0O0O0000 .extractall (OO00OO00O00O0OOO0 )#line:912
        for OO0OOOO0OO0O0OO0O in os .listdir (OO00OO00O00O0OOO0 ):#line:944
            if OO0OOOO0OO0O0OO0O .endswith (".step"):#line:946
                OOOOO0O0O00000000 =os .path .join (OO00OO00O00O0OOO0 ,OO0OOOO0OO0O0OO0O )#line:948
                copyfile (OOOOO0O0O00000000 ,os .path .join (OOOO00OO0OOO00OO0 .snapeda_threedee_models_dir ,OO0OOOO0OO0O0OO0O ))#line:949
            if OO0OOOO0OO0O0OO0O .endswith (".kicad_mod"):#line:951
                OOOO00OO0OOO00OO0 .kicad_mod_filename =OO0OOOO0OO0O0OO0O [:-10 ]#line:952
                OO00OO0O00OOO0OO0 =os .path .join (OO00OO00O00O0OOO0 ,OO0OOOO0OO0O0OO0O )#line:953
                copyfile (OO00OO0O00OOO0OO0 ,os .path .join (OOOO00OO0OOO00OO0 .snapeda_library_abs_dir ,OO0OOOO0OO0O0OO0O ))#line:954
            if OO0OOOO0OO0O0OO0O .endswith (".lib"):#line:956
                O0OOO0O0O00OO0O00 =False #line:958
                with open (os .path .join (OO00OO00O00O0OOO0 ,OO0OOOO0OO0O0OO0O ),"r+")as O0OO0O0000OO00O0O :#line:959
                    OOOOOO0OOO0O0O0OO =O0OO0O0000OO00O0O .readlines ()#line:960
                    O0O0O0OO0OOOO000O =[]#line:961
                    for O0OOO0OO0OOOOOO00 in OOOOOO0OOO0O0O0OO :#line:962
                        if 'F2 "'in O0OOO0OO0OOOOOO00 :#line:963
                            O0O0OO00OO0000OO0 =O0OOO0OO0OOOOOO00 .split ('"')#line:964
                            OO0O0000O00O0OO00 =O0O0OO00OO0000OO0 [0 ]+'"'+OO0OOOOOO0O0OO00O ['kicad_library_name']+':'+O0O0OO00OO0000OO0 [1 ]+'"'+O0O0OO00OO0000OO0 [2 ]#line:965
                            O0OOO0OO0OOOOOO00 =OO0O0000O00O0OO00 #line:966
                            O0OOO0O0O00OO0O00 =True #line:967
                        O0O0O0OO0OOOO000O +=O0OOO0OO0OOOOOO00 #line:968
                if O0OOO0O0O00OO0O00 :#line:969
                    with open (os .path .join (OO00OO00O00O0OOO0 ,OO0OOOO0OO0O0OO0O ),"w")as O0OO0O0000OO00O0O :#line:970
                        O0OO0O0000OO00O0O .writelines (O0O0O0OO0OOOO000O )#line:971
                O0OO00O000O0O000O =os .path .join (OO00OO00O00O0OOO0 ,OO0OOOO0OO0O0OO0O )#line:973
                copyfile (O0OO00O000O0O000O ,os .path .join (OOOO00OO0OOO00OO0 .snapeda_library_dir ,OO0OOOO0OO0O0OO0O ))#line:974
                if OOOO00OO0OOO00OO0 .is_windows :#line:976
                    OOOO00OO0OOO00OO0 .sym_lib_table_dir =os .path .join (os .getenv ('APPDATA'),'kicad','sym-lib-table')#line:979
                else :#line:980
                    OOOO00OO0OOO00OO0 .sym_lib_table_dir =os .path .join (os .path .expanduser ("~"),'.config','kicad','sym-lib-table')#line:984
                if (os .path .exists (OOOO00OO0OOO00OO0 .sym_lib_table_dir )!=True ):#line:986
                    OO0000OOO0O0OO000 ='(sym_lib_table\n\n)'#line:987
                    with open (OOOO00OO0OOO00OO0 .sym_lib_table_dir ,'w')as OOOO0OO0O00OO0OOO :#line:988
                        OOOO0OO0O00OO0OOO .write (OO0000OOO0O0OO000 )#line:989
                        OOOO0OO0O00OO0OOO .close #line:990
                with open (OOOO00OO0OOO00OO0 .sym_lib_table_dir ,"r+")as O0OO0O0000OO00O0O :#line:992
                    OOOOOO000O0O000O0 =O0OO0O0000OO00O0O .read ()#line:993
                    OO0O0000O00O0OO00 =('  (lib (name '+os .path .splitext (OO0OOOO0OO0O0OO0O )[0 ]+')(type Legacy)(uri "'+OOOO00OO0OOO00OO0 .snapeda_library_dir +'\\'+str (OO0OOOO0OO0O0OO0O )+'")(options "")(descr ""))')#line:994
                    OO0O0000O00O0OO00 =OO0O0000O00O0OO00 .replace ("'","")#line:995
                    OO0O0000O00O0OO00 =OO0O0000O00O0OO00 .replace ("\\","/")#line:996
                    if OO0O0000O00O0OO00 not in OOOOOO000O0O000O0 :#line:997
                        OO0O0000O00O0OO00 =('  (lib (name '+os .path .splitext (OO0OOOO0OO0O0OO0O )[0 ]+')(type Legacy)(uri "'+OOOO00OO0OOO00OO0 .snapeda_library_dir +'\\'+str (OO0OOOO0OO0O0OO0O )+'")(options "")(descr ""))')+"\n\n)"#line:998
                        OO0O0000O00O0OO00 =OO0O0000O00O0OO00 .replace ("'","")#line:999
                        OO0O0000O00O0OO00 =OO0O0000O00O0OO00 .replace ("\\","/")#line:1000
                        OOOOO0000O0O0O000 =OOOOOO000O0O000O0 [:-2 ]+OO0O0000O00O0OO00 #line:1001
                        O0OO0O0000OO00O0O .seek (0 )#line:1002
                        O0OO0O0000OO00O0O .write (OOOOO0000O0O0O000 )#line:1003
                        O0OO0O0000OO00O0O .truncate ()#line:1004
        shutil .rmtree (OOOO00000OOOOO00O )#line:1006
        OOOO00OO0OOO00OO0 .download_button .config (state ="normal",text ="Download")#line:1158
        OOOO00OO0OOO00OO0 .is_downloading =False #line:1159
        if IS_SETTING_WINDOW_OPEN is False :#line:1160
            OOOO00OO0OOO00OO0 .parent .is_help_me_window =False #line:1161
            AfterDownloadView (OOOO00OO0OOO00OO0 .parent ,OOOO00OO0OOO00OO0 .flip_table_dir ,OOOO00OO0OOO00OO0 .proj_flip_table_dir ,OOOO00OO0OOO00OO0 .snapeda_library_abs_dir ,OOOO00OO0OOO00OO0 .kicad_mod_filename )#line:1162
    def winapi_path (O0OOO00OO0O0OO00O ,OO0O0OOOOOOOOOOOO ,encoding =None ):#line:1164
        if (not isinstance (OO0O0OOOOOOOOOOOO ,unicode )and encoding is not None ):#line:1165
            OO0O0OOOOOOOOOOOO =OO0O0OOOOOOOOOOOO .decode (encoding )#line:1166
        O00OOO0000O0OOO00 =os .path .abspath (OO0O0OOOOOOOOOOOO )#line:1167
        if O00OOO0000O0OOO00 .startswith (u"\\\\"):#line:1168
            return u"\\\\?\\UNC\\"+O00OOO0000O0OOO00 [2 :]#line:1169
        return u"\\\\?\\"+O00OOO0000O0OOO00 #line:1170
    def contact_us (O00O0000O00000OOO ):#line:1172
        webbrowser .open ("https://www.snapeda.com/about/#contact_us",new =2 )#line:1173
    def about_snapeda (O0OO00OO00OOO0O0O ):#line:1175
        webbrowser .open ("https://www.snapeda.com/about/",new =2 )#line:1176
    def view_on_snapeda (O00OO0OOOOOOO00OO ,O0O00O0O0OOOOO0O0 ):#line:1178
        webbrowser .open ("https://www.snapeda.com%s?ref=kicad"%(O0O00O0O0OOOOO0O0 [:-10 ]+'datasheet/'),new =2 )#line:1179
    def how_it_works_callback (O0OO000O00OO00000 ,O0OOO00000000OOO0 ):#line:1181
        global IS_SETTING_WINDOW_OPEN #line:1182
        if IS_SETTING_WINDOW_OPEN is False :#line:1183
            O0OO000O00OO00000 .parent .is_help_me_window =False #line:1184
            InfoView (O0OO000O00OO00000 .parent )#line:1185
    def logout_callback (OOO000O000OOOO00O ,OOO000O00OO00O00O ):#line:1197
        try :#line:1198
            if OOO000O000OOOO00O .is_windows :#line:1199
                OOO000O000OOOO00O .windata_dir =os .path .join (os .getenv ('HOMEDRIVE'),os .getenv ('HOMEPATH'),"SnapEDA Kicad Plugin")#line:1202
                OOO000O000OOOO00O .appdata_dir =os .path .join (OOO000O000OOOO00O .windata_dir ,"App")#line:1203
                O0OOOOOOOOOO0O0O0 =os .path .join (OOO000O000OOOO00O .appdata_dir ,".token")#line:1204
                os .remove (O0OOOOOOOOOO0O0O0 )#line:1205
            elif OOO000O000OOOO00O .is_mac :#line:1206
                OOO000O000OOOO00O .macdata_dir =os .path .join (os .path .expanduser ("~"),"Documents","SnapEDA Kicad Plugin")#line:1207
                OOO000O000OOOO00O .appdata_dir =os .path .join (OOO000O000OOOO00O .macdata_dir ,"App")#line:1208
                O0OOOOOOOOOO0O0O0 =os .path .join (OOO000O000OOOO00O .appdata_dir ,".token")#line:1209
                os .remove (O0OOOOOOOOOO0O0O0 )#line:1210
            else :#line:1211
                OOO000O000OOOO00O .dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:1212
                O0OOOOOOOOOO0O0O0 =os .path .join (OOO000O000OOOO00O .dir_path ,".token")#line:1213
                os .remove (O0OOOOOOOOOO0O0O0 )#line:1214
        except :#line:1215
            print ('Error removing token.')#line:1216
        for OOO0O00O0000O0O0O in range (5 ):#line:1217
            for OOO0OO00O0OO0O00O in OOO000O000OOOO00O .parent .grid_slaves (row =OOO0O00O0000O0O0O ,column =0 ):#line:1218
                OOO0OO00O0OO0O00O .destroy ()#line:1219
        LoginScreen (OOO000O000OOOO00O .master )#line:1220
        return #line:1221
    def update_process (OO0O0OOOO0OO0000O ):#line:1223
        OO0O0OOOO0OO0000O .status_text .set ("Downloading update...")#line:1225
        O0OOOO0O0OO000OOO =os .path .join (OO0O0OOOO0OO0000O .kicad_library_dir ,'temp')#line:1226
        if not os .path .exists (O0OOOO0O0OO000OOO ):#line:1227
                os .makedirs (O0OOOO0O0OO000OOO )#line:1228
        if sys .version_info [0 ]==3 :#line:1229
            with urllib .request .urlopen ('https://snapeda.s3.amazonaws.com/plugins/kicad/SnapEDA-KiCad-Plugin.zip')as O000OO0O000OO00OO ,open (os .path .join (O0OOOO0O0OO000OOO ,'SnapEDA-KiCad-Plugin.zip'),'wb')as OOO00O000OOO00OOO :#line:1230
                shutil .copyfileobj (O000OO0O000OO00OO ,OOO00O000OOO00OOO )#line:1231
        else :#line:1232
            O000O0OOO00O0OO00 =urllib2 .urlopen ('https://snapeda.s3.amazonaws.com/plugins/kicad/SnapEDA-KiCad-Plugin.zip')#line:1233
            with open (os .path .join (O0OOOO0O0OO000OOO ,'SnapEDA-KiCad-Plugin.zip'),"wb")as OO0OO0O0OO0OOO0OO :#line:1234
                shutil .copyfileobj (O000O0OOO00O0OO00 ,OO0OO0O0OO0OOO0OO )#line:1235
        OO0O0OOOO0OO0000O .status_text .set ("Extracting package...")#line:1237
        with zipfile .ZipFile (os .path .join (O0OOOO0O0OO000OOO ,'SnapEDA-KiCad-Plugin.zip'))as OO0O0OO0OOO000000 :#line:1239
            OO0O0OO0OOO000000 .extractall (O0OOOO0O0OO000OOO )#line:1240
        OO0O0OOOO0OO0000O .status_text .set ("Copying files...")#line:1242
        for O00000OO0O0OOO000 in os .listdir (O0OOOO0O0OO000OOO ):#line:1244
            if O00000OO0O0OOO000 .endswith (".py"):#line:1245
                copyfile (os .path .join (O0OOOO0O0OO000OOO ,O00000OO0O0OOO000 ),os .path .join (os .path .dirname (os .path .realpath (__file__ )),O00000OO0O0OOO000 ))#line:1246
        shutil .rmtree (O0OOOO0O0OO000OOO )#line:1248
        OO0O0OOOO0OO0000O .status_text .set ("Update complete.")#line:1250
        OO0O0OOOO0OO0000O .header_text .set ("UPDATE COMPLETE")#line:1252
        OO0O0OOOO0OO0000O .subheader_text .set ("Update successful. Please restart SnapEDA, refresh the plugins, then open SnapEDA.")#line:1253
        OO0O0OOOO0OO0000O .status_text .set ("")#line:1254
    def update_callback (O0O0O00OO00O000OO ,OOOO00OO0O000O00O ):#line:1257
        try :#line:1259
            O0O0OOOO000O000O0 =os .getuid ()==0 #line:1260
        except AttributeError :#line:1261
            O0O0OOOO000O000O0 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:1262
        if not O0O0OOOO000O000O0 :#line:1264
            if O0O0O00OO00O000OO .is_windows :#line:1265
                tkMessageBox .showwarning ("Update","Please restart KiCAD as administrator, then update again.")#line:1266
                return #line:1267
        O0O0O00OO00O000OO .update_container =tk .Frame (O0O0O00OO00O000OO .parent ,bg ="#ff761a")#line:1272
        O0O0O00OO00O000OO .update_container .grid (row =0 ,column =0 ,sticky ="NEWS")#line:1273
        O0O0O00OO00O000OO .update_container .grid_columnconfigure (0 ,weight =1 )#line:1274
        for O00OO0OOOO00OO00O in range (4 ):#line:1275
            O0O0O00OO00O000OO .update_container .grid_rowconfigure (O00OO0OOOO00OO00O ,weight =1 ,uniform ="foo")#line:1276
        O0O0O00OO00O000OO .header_container =tk .Frame (O0O0O00OO00O000OO .update_container ,bg ="#ff761a")#line:1278
        O0O0O00OO00O000OO .header_container .grid (row =1 ,column =0 ,columnspan =1 ,sticky ="NEWS")#line:1279
        O0O0O00OO00O000OO .header_container .grid_columnconfigure (0 ,weight =1 )#line:1280
        for O00OO0OOOO00OO00O in range (3 ):#line:1281
            O0O0O00OO00O000OO .header_container .grid_rowconfigure (O00OO0OOOO00OO00O ,weight =1 ,uniform ="foo")#line:1282
        O0O0O00OO00O000OO .header_text =tk .StringVar ()#line:1284
        O0O0O00OO00O000OO .header_text .set ("UPDATING...")#line:1285
        O0O0O00OO00O000OO .header_label =tk .Label (O0O0O00OO00O000OO .header_container ,bg ="#ff761a",fg ="white",textvariable =O0O0O00OO00O000OO .header_text ,justify =tk .CENTER ,font =("Open Sans","18","bold"))#line:1286
        O0O0O00OO00O000OO .header_label .grid (row =0 ,column =0 ,columnspan =1 ,sticky ="NEWS")#line:1287
        O0O0O00OO00O000OO .subheader_text =tk .StringVar ()#line:1289
        O0O0O00OO00O000OO .subheader_text .set ("This may take a while, about 3-5 minutes. Mind to have a coffee break?")#line:1290
        O0O0O00OO00O000OO .subheader_label =tk .Label (O0O0O00OO00O000OO .header_container ,textvariable =O0O0O00OO00O000OO .subheader_text ,fg ="white",bg ="#ff761a",font =("Open Sans","13"))#line:1291
        O0O0O00OO00O000OO .subheader_label .grid (row =1 ,column =0 ,sticky ="NEW")#line:1292
        O0O0O00OO00O000OO .status_text =tk .StringVar ()#line:1294
        O0O0O00OO00O000OO .status_text .set ("Starting update...")#line:1295
        O0O0O00OO00O000OO .status_label =tk .Label (O0O0O00OO00O000OO .header_container ,textvariable =O0O0O00OO00O000OO .status_text ,fg ="white",bg ="#ff761a",font =("Open Sans","13","italic"))#line:1296
        O0O0O00OO00O000OO .status_label .grid (row =2 ,column =0 ,sticky ="NEW")#line:1297
        O0O0O00OO00O000OO .update_thread =threading .Thread (target =O0O0O00OO00O000OO .update_process )#line:1299
        O0O0O00OO00O000OO .update_thread .setDaemon (True )#line:1300
        O0O0O00OO00O000OO .update_thread .start ()#line:1301
    def help_me_callback (O0000O00O0O00OOOO ,OOO00000O0O0OO0O0 ):#line:1303
        global IS_SETTING_WINDOW_OPEN #line:1304
        if IS_SETTING_WINDOW_OPEN is False :#line:1305
            O0000O00O0O00OOOO .parent .is_help_me_window =True #line:1306
            InfoView (O0000O00O0O00OOOO .parent )#line:1307
    def home_callback (OO0O0O0OO000OO000 ,OO0OO0O0OOO00O0OO ):#line:1311
        for O0O0O0OOOOOO000O0 in range (5 ):#line:1312
            for OOOOO0O0OOOO0O00O in OO0O0O0OO000OO000 .parent .grid_slaves (row =O0O0O0OOOOOO000O0 ,column =0 ):#line:1313
                OOOOO0O0OOOO0O00O .destroy ()#line:1314
        WelcomeScreen (OO0O0O0OO000OO000 .parent )#line:1315
    def setting_callback (OO0000OO00O000OOO ,O0OO0OO0OO0O000O0 ):#line:1317
        global IS_SETTING_WINDOW_OPEN #line:1318
        if IS_SETTING_WINDOW_OPEN is False :#line:1319
            SettingsView (OO0000OO00O000OOO .parent )#line:1320
    def next_page (O0OO0OO0O0000OOO0 ,O00OOO0O000000000 ):#line:1322
        if O0OO0OO0O0000OOO0 .current_page <O0OO0OO0O0000OOO0 .max_page :#line:1323
            O0OO0OO0O0000OOO0 .current_page +=1 #line:1324
            O0OO0OO0O0000OOO0 .search_data (O00OOO0O000000000 ,current_page =O0OO0OO0O0000OOO0 .current_page )#line:1325
    def prev_page (O0OO0O000000O0OO0 ,OO00OO0000O0OO0O0 ):#line:1327
        if O0OO0O000000O0OO0 .current_page >1 :#line:1328
            O0OO0O000000O0OO0 .current_page -=1 #line:1329
            O0OO0O000000O0OO0 .search_data (OO00OO0000O0OO0O0 ,current_page =O0OO0O000000O0OO0 .current_page )#line:1330
    def on_tree_select (O00000O0O0O00O00O ,OOO0OO00000OOOO0O ,index =None ):#line:1333
        if not O00000O0O0O00O00O .is_loading :#line:1338
            O00000O0O0O00O00O .is_loading =True #line:1339
            O00000O0O0O00O00O .get_component_thread =threading .Thread (target =O00000O0O0O00O00O .get_component ,args =(OOO0OO00000OOOO0O ,index ))#line:1343
            O00000O0O0O00O00O .get_component_thread .start ()#line:1344
    def model_2D_callback (O0O00OO000OOOOO00 ,OO000OO0OO0O0O0OO ,OOOOO00O0000OOOOO ):#line:1348
        global IS_3D_TAB_OPEN #line:1349
        IS_3D_TAB_OPEN =False #line:1350
        O0O00OO000OOOOO00 .model_3D_underline .destroy ()#line:1352
        O0O00OO000OOOOO00 .model_3D_text .configure (bg ="#EEEEEE",fg ="#333333")#line:1353
        O0O00OO000OOOOO00 .model_3D_text .grid (row =0 ,column =1 ,sticky ="NEWS",padx =1 ,pady =1 )#line:1354
        O0O00OO000OOOOO00 .model_3D_text .bind ('<Button-1>',lambda O0O0000OO0OO0000O ,index =OOOOO00O0000OOOOO :O0O00OO000OOOOO00 .model_3D_callback (O0O0000OO0OO0000O ,index ))#line:1355
        O0O00OO000OOOOO00 .model_2D_underline =tk .Label (O0O00OO000OOOOO00 .model_tab_frame ,bg ="#FF761A")#line:1357
        O0O00OO000OOOOO00 .model_2D_underline .grid (row =0 ,column =0 ,sticky ="NEWS",pady =(1 ,0 ),padx =1 )#line:1358
        O0O00OO000OOOOO00 .model_2D_text .destroy ()#line:1359
        O0O00OO000OOOOO00 .model_2D_text =tk .Label (O0O00OO000OOOOO00 .model_tab_frame ,bg ="white",fg ="#FF761A",text ="2D Model",font =("Open Sans",10 ),cursor ="hand2")#line:1360
        O0O00OO000OOOOO00 .model_2D_text .grid (row =0 ,column =0 ,sticky ="NEWS",padx =1 ,pady =(1 ,4 ))#line:1361
        O0O00OO000OOOOO00 .symbol_view .destroy ()#line:1364
        O0O00OO000OOOOO00 .symbol_frame =tk .Frame (O0O00OO000OOOOO00 .details_frame ,bg ="white")#line:1366
        O0O00OO000OOOOO00 .symbol_frame .grid (row =4 ,column =0 ,rowspan =3 ,sticky ="NEWS",padx =1 ,pady =(0 ,1 ))#line:1367
        O0O00OO000OOOOO00 .symbol_frame .grid_columnconfigure (0 ,weight =1 )#line:1368
        O0O00OO000OOOOO00 .symbol_frame .grid_rowconfigure (0 ,weight =1 )#line:1369
        O0O00OO000OOOOO00 .model_canvas =tk .Canvas (O0O00OO000OOOOO00 .symbol_frame ,bg ="white")#line:1371
        O0O00OO000OOOOO00 .model_canvas .grid (row =0 ,column =0 ,sticky ="NEWS")#line:1372
        O0OOOO00000OOO0OO =ttk .Style ()#line:1373
        O0OOOO00000OOO0OO .theme_use ('clam')#line:1374
        O0OOOO00000OOO0OO .configure ("snapeda.Vertical.TScrollbar",gripcount =0 ,background ="#FF8330",troughcolor ='#C4C4C4',lightcolor ='#C4C4C4',darkcolor ='#C4C4C4',bordercolor ="#C4C4C4",borderwidth =0 ,relief =tk .FLAT )#line:1375
        O0OOOO00000OOO0OO .map ('snapeda.Vertical.TScrollbar',foreground =[('disabled','#C4C4C4'),('pressed','#FF8330'),('active','#FF8330')],background =[('disabled','#C4C4C4'),('pressed','!focus','#FF8330'),('active','#FF8330')],highlightcolor =[('focus','#C4C4C4'),('!focus','#C4C4C4')],)#line:1383
        O0OOOO00000OOO0OO .layout ('snapeda.Vertical.TScrollbar',[('Vertical.Scrollbar.trough',{'children':[('Vertical.Scrollbar.thumb',{'expand':'1','sticky':'nswe'})],'sticky':'ns'})])#line:1385
        O0O00OO000OOOOO00 .model_scrollbar =ttk .Scrollbar (O0O00OO000OOOOO00 .symbol_frame ,orient ="vertical",command =O0O00OO000OOOOO00 .model_canvas .yview ,style ="snapeda.Vertical.TScrollbar")#line:1386
        O0O00OO000OOOOO00 .model_scrollbar .grid (row =0 ,column =1 ,sticky ='NS')#line:1387
        O0O00OO000OOOOO00 .model_frame =tk .Frame (O0O00OO000OOOOO00 .model_canvas ,bg ="white")#line:1388
        O0O00OO000OOOOO00 .model_frame .bind ("<Configure>",lambda OO0OO0OO0O0000OO0 :O0O00OO000OOOOO00 .model_canvas .configure (scrollregion =O0O00OO000OOOOO00 .model_canvas .bbox ("all")))#line:1389
        O0O00OO000OOOOO00 .model_canvas .create_window ((0 ,0 ),window =O0O00OO000OOOOO00 .model_frame ,anchor =tk .CENTER )#line:1390
        O0O00OO000OOOOO00 .model_canvas .configure (yscrollcommand =O0O00OO000OOOOO00 .model_scrollbar .set )#line:1391
        if O0O00OO000OOOOO00 .has_model :#line:1393
            O0O00OO000OOOOO00 .symbol_view =tk .Label (O0O00OO000OOOOO00 .model_frame ,bg ="white",image =O0O00OO000OOOOO00 .symbol_image )#line:1394
            O0O00OO000OOOOO00 .symbol_view .grid (row =0 ,column =0 ,sticky ="NEWS",padx =(65 ,65 ))#line:1395
        else :#line:1396
            O0O00OO000OOOOO00 .symbol_view =tk .Frame (O0O00OO000OOOOO00 .model_frame ,bg ="white")#line:1397
            O0O00OO000OOOOO00 .symbol_view .columnconfigure (0 ,weight =1 ,uniform ='foo')#line:1398
            O0O00OO000OOOOO00 .symbol_view .grid (row =0 ,column =0 ,sticky ='NEWS',padx =(60 ,60 ))#line:1399
            tk .Label (O0O00OO000OOOOO00 .symbol_view ,bg ="white",image =O0O00OO000OOOOO00 .ghost_2D_im ).grid (row =0 ,column =0 ,sticky ="NEWS")#line:1400
            O0O00OO000OOOOO00 .request_button =tk .Label (O0O00OO000OOOOO00 .symbol_view ,bg ="white",image =O0O00OO000OOOOO00 .request_button_img ,cursor ="hand2")#line:1401
            O0O00OO000OOOOO00 .request_button .grid (row =1 ,column =0 ,sticky ="NEWS",pady =(0 ,60 ))#line:1402
            O0O00OO000OOOOO00 .request_button .bind ('<Button-1>',O0O00OO000OOOOO00 .request_now_button_callback )#line:1403
        if O0O00OO000OOOOO00 .has_package :#line:1405
            OOO0OO00O0O0000OO =tk .Label (O0O00OO000OOOOO00 .model_frame ,bg ="white",image =O0O00OO000OOOOO00 .package_image )#line:1406
            OOO0OO00O0O0000OO .grid (row =1 ,column =0 ,sticky ="NEWS")#line:1407
        else :#line:1408
            OOO0OO00O0O0000OO =tk .Frame (O0O00OO000OOOOO00 .model_frame ,bg ="white")#line:1409
            OOO0OO00O0O0000OO .columnconfigure (0 ,weight =1 ,uniform ='foo')#line:1410
            OOO0OO00O0O0000OO .rowconfigure (0 ,weight =2 ,uniform ='foo')#line:1411
            OOO0OO00O0O0000OO .rowconfigure (0 ,weight =1 ,uniform ='foo')#line:1412
            OOO0OO00O0O0000OO .grid (row =1 ,column =0 ,sticky ='NEWS')#line:1413
            tk .Label (OOO0OO00O0O0000OO ,bg ="white",image =O0O00OO000OOOOO00 .ghost_im ).grid (row =0 ,column =0 ,sticky ="NEWS")#line:1414
            tk .Label (OOO0OO00O0O0000OO ,bg ="white",text ='No Package',font =("Open Sans",11 )).grid (row =1 ,column =0 ,sticky ="NEWS",pady =(0 ,15 ))#line:1415
        O0O00OO000OOOOO00 .model_frame .update_idletasks ()#line:1417
        O0O00OO000OOOOO00 .model_tab_frame .update_idletasks ()#line:1418
    def model_3D_callback (O0O0OOO0OOO000OOO ,O0O0O0OO0OO0OO0O0 ,O00OO00OOOO000O00 ):#line:1420
        global IS_3D_TAB_OPEN #line:1421
        IS_3D_TAB_OPEN =True #line:1422
        O0O0OOO0OOO000OOO .symbol_view .destroy ()#line:1424
        O0O0OOO0OOO000OOO .symbol_frame =tk .Frame (O0O0OOO0OOO000OOO .details_frame ,bg ="white")#line:1426
        O0O0OOO0OOO000OOO .symbol_frame .grid (row =4 ,column =0 ,rowspan =3 ,sticky ="NEWS",padx =1 ,pady =(0 ,1 ))#line:1427
        O0O0OOO0OOO000OOO .symbol_frame .grid_columnconfigure (0 ,weight =1 )#line:1428
        O0O0OOO0OOO000OOO .symbol_frame .grid_rowconfigure (0 ,weight =1 )#line:1429
        O0O0OOO0OOO000OOO .model_canvas =tk .Canvas (O0O0OOO0OOO000OOO .symbol_frame ,bg ="white")#line:1431
        O0O0OOO0OOO000OOO .model_canvas .grid (row =0 ,column =0 ,sticky ="NEWS")#line:1432
        OOO0000OOO0OO0O00 =ttk .Style ()#line:1433
        OOO0000OOO0OO0O00 .theme_use ('clam')#line:1434
        OOO0000OOO0OO0O00 .configure ("snapeda.Vertical.TScrollbar",gripcount =0 ,background ="#FF8330",troughcolor ='#C4C4C4',lightcolor ='#C4C4C4',darkcolor ='#C4C4C4',bordercolor ="#C4C4C4",borderwidth =0 ,relief =tk .FLAT )#line:1435
        OOO0000OOO0OO0O00 .map ('snapeda.Vertical.TScrollbar',foreground =[('disabled','#C4C4C4'),('pressed','#FF8330'),('active','#FF8330')],background =[('disabled','#C4C4C4'),('pressed','!focus','#FF8330'),('active','#FF8330')],highlightcolor =[('focus','#C4C4C4'),('!focus','#C4C4C4')],)#line:1443
        OOO0000OOO0OO0O00 .layout ('snapeda.Vertical.TScrollbar',[('Vertical.Scrollbar.trough',{'children':[('Vertical.Scrollbar.thumb',{'expand':'1','sticky':'nswe'})],'sticky':'ns'})])#line:1445
        O0O0OOO0OOO000OOO .model_scrollbar =ttk .Scrollbar (O0O0OOO0OOO000OOO .symbol_frame ,orient ="vertical",command =O0O0OOO0OOO000OOO .model_canvas .yview ,style ="snapeda.Vertical.TScrollbar")#line:1446
        O0O0OOO0OOO000OOO .model_scrollbar .grid (row =0 ,column =1 ,sticky ='NS')#line:1447
        O0O0OOO0OOO000OOO .model_frame =tk .Frame (O0O0OOO0OOO000OOO .model_canvas ,bg ="white")#line:1448
        O0O0OOO0OOO000OOO .model_frame .bind ("<Configure>",lambda OO0OOO00O0OOO000O :O0O0OOO0OOO000OOO .model_canvas .configure (scrollregion =O0O0OOO0OOO000OOO .model_canvas .bbox ("all")))#line:1449
        O0O0OOO0OOO000OOO .model_canvas .create_window ((0 ,0 ),window =O0O0OOO0OOO000OOO .model_frame ,anchor =tk .CENTER )#line:1450
        O0O0OOO0OOO000OOO .model_canvas .configure (yscrollcommand =O0O0OOO0OOO000OOO .model_scrollbar .set )#line:1451
        O0O0OOO0OOO000OOO .threedee_text =tk .StringVar ()#line:1454
        O0O0OOO0OOO000OOO .threedee_text .set ("Please wait for the 3D image to load.")#line:1455
        tk .Label (O0O0OOO0OOO000OOO .model_frame ,bg ="white",textvariable =O0O0OOO0OOO000OOO .threedee_text ).grid (row =0 ,column =0 ,sticky ="NEWS")#line:1456
        O0O0OOO0OOO000OOO .model_2D_underline .destroy ()#line:1460
        O0O0OOO0OOO000OOO .model_2D_text .configure (bg ="#EEEEEE",fg ="#333333")#line:1461
        O0O0OOO0OOO000OOO .model_2D_text .grid (row =0 ,column =0 ,sticky ="NEWS",padx =1 ,pady =1 )#line:1462
        O0O0OOO0OOO000OOO .model_2D_text .bind ('<Button-1>',lambda OO00OOO00O000000O ,index =O00OO00OOOO000O00 :O0O0OOO0OOO000OOO .model_2D_callback (OO00OOO00O000000O ,index ))#line:1463
        O0O0OOO0OOO000OOO .model_3D_underline =tk .Label (O0O0OOO0OOO000OOO .model_tab_frame ,bg ="#FF761A")#line:1465
        O0O0OOO0OOO000OOO .model_3D_underline .grid (row =0 ,column =1 ,sticky ="NEWS",pady =(1 ,0 ),padx =1 )#line:1466
        O0O0OOO0OOO000OOO .model_3D_text .destroy ()#line:1467
        O0O0OOO0OOO000OOO .model_3D_text =tk .Label (O0O0OOO0OOO000OOO .model_tab_frame ,bg ="white",fg ="#FF761A",text ="3D Model",font =("Open Sans",10 ),cursor ="hand2")#line:1468
        O0O0OOO0OOO000OOO .model_3D_text .grid (row =0 ,column =1 ,sticky ="NEWS",padx =1 ,pady =(1 ,4 ))#line:1469
        O0O0OOO0OOO000OOO .symbol_view .destroy ()#line:1471
        if O0O0OOO0OOO000OOO .threedmodel_medium_image :#line:1473
            O0O0OOO0OOO000OOO .threedee_text .set ("")#line:1474
            O0O0OOO0OOO000OOO .threedee_model_img =tk .Label (O0O0OOO0OOO000OOO .model_frame ,bg ="white",image =O0O0OOO0OOO000OOO .threedmodel_medium_image )#line:1475
            O0O0OOO0OOO000OOO .threedee_model_img .grid (row =0 ,column =0 ,sticky ="NEWS",padx =(400 ,60 ))#line:1476
            O0O0OOO0OOO000OOO .model_frame .update_idletasks ()#line:1477
        else :#line:1478
            O0O0OOO0OOO000OOO .threedee_text .set ("No 3D preview available.")#line:1479
        O0O0OOO0OOO000OOO .details_frame .update_idletasks ()#line:1481
    def request_now_button_callback (OO0O0O0OO0O0O0OOO ,O0OO000O00O0000OO ):#line:1488
        webbrowser .open ("https://www.snapeda.com/instapart/",new =2 )#line:1489
    def on_button_active (O00OO00O0O0O0O000 ,O0O00O00OO0O000O0 ,OO0OO0OOOO000O00O ):#line:1491
        OO0OO0OOOO000O00O .config (fg ="#ff761a",bg ="white")#line:1492
    def on_button_inactive (OO00OOOOOO0OOO0OO ,O0O00O00O0OOO0O00 ,OOO000O000O0OOO0O ):#line:1494
        OOO000O000O0OOO0O .config (bg ="#ff761a",fg ="white")#line:1495
    def download_threedee_thread (O000O0OOOOOOO0O0O ,OO00000000OO0O0O0 ):#line:1497
        global IS_3D_TAB_OPEN #line:1499
        if O000O0OOOOOOO0O0O .intense_caverns_img_dir [OO00000000OO0O0O0 ]is None and not O000O0OOOOOOO0O0O .intense_caverns_thread_started [OO00000000OO0O0O0 ]:#line:1500
            OO0000O000OOO0OOO =O000O0OOOOOOO0O0O .intense_caverns_links [OO00000000OO0O0O0 ]#line:1501
            if len (OO0000O000OOO0OOO )!=0 :#line:1502
                O000O0OOOOOOO0O0O .intense_caverns_thread_started [OO00000000OO0O0O0 ]=True #line:1503
                print ('start download_threedee_thread')#line:1504
                OO0000O000OOO0OOO ="http://screeenly.com/api/v1/fullsize"#line:1505
                O00O000OOO0O00OOO ={'key':'AMln0sZduFx8WVg3v8KVnlZAUgOcYgAhJFBAIJZXB90GZLo2JP','url':OO0000O000OOO0OOO ,'delay':4 ,}#line:1510
                try :#line:1511
                    OOO000O00O00O0O00 =time .time ()#line:1512
                    if sys .version_info [0 ]==3 :#line:1514
                        print ('taking snapshot')#line:1515
                        OOOO0O000O00OO00O =urllib .parse .urlencode (O00O000OOO0O00OOO ).encode ("utf-8")#line:1516
                        O000OOO0O00000O00 =urllib .request .Request (OO0000O000OOO0OOO ,OOOO0O000O00OO00O )#line:1517
                        O00OOOO0O00O0OO00 =urllib .request .urlopen (O000OOO0O00000O00 ).read ()#line:1518
                        OOOO0O000O00OO00O =json .loads (O00OOOO0O00O0OO00 )#line:1519
                        OO0000O000OOO0OOO =OOOO0O000O00OO00O ['path']#line:1520
                        O0000O000O00000OO =OO0000O000OOO0OOO [OO0000O000OOO0OOO .rfind ('/')+1 :]#line:1521
                        OOO00OO0OO0O000OO =os .path .join (O000O0OOOOOOO0O0O .appdata_dir ,O0000O000O00000OO )#line:1522
                        print ('saving snapshot')#line:1523
                        urllib .request .urlretrieve (OO0000O000OOO0OOO ,OOO00OO0OO0O000OO )#line:1524
                        O000O0OOOOOOO0O0O .intense_caverns_img_dir [OO00000000OO0O0O0 ]=OOO00OO0OO0O000OO #line:1525
                    else :#line:1526
                        print ('taking snapshot')#line:1527
                        OOOO0O000O00OO00O =urllib .urlencode (O00O000OOO0O00OOO )#line:1528
                        O000OOO0O00000O00 =urllib2 .Request (OO0000O000OOO0OOO ,OOOO0O000O00OO00O )#line:1529
                        O00OOOO0O00O0OO00 =urllib2 .urlopen (O000OOO0O00000O00 ).read ()#line:1530
                        OOOO0O000O00OO00O =json .loads (O00OOOO0O00O0OO00 )#line:1531
                        OO0000O000OOO0OOO =OOOO0O000O00OO00O ['path']#line:1532
                        O0000O000O00000OO =OO0000O000OOO0OOO [OO0000O000OOO0OOO .rfind ('/')+1 :]#line:1533
                        OOO00OO0OO0O000OO =os .path .join (O000O0OOOOOOO0O0O .appdata_dir ,O0000O000O00000OO )#line:1534
                        print ('saving snapshot')#line:1535
                        urllib .urlretrieve (OO0000O000OOO0OOO ,OOO00OO0OO0O000OO )#line:1536
                        O000O0OOOOOOO0O0O .intense_caverns_img_dir [OO00000000OO0O0O0 ]=OOO00OO0OO0O000OO #line:1537
                    print ('end download_threedee_thread')#line:1538
                    O0OO0000OO00000OO =time .time ()#line:1539
                    print ("Execution time: "+str (O0OO0000OO00000OO -OOO000O00O00O0O00 )+"s")#line:1540
                except :#line:1541
                    O000O0OOOOOOO0O0O .intense_caverns_img_dir [OO00000000OO0O0O0 ]=os .path .join (O000O0OOOOOOO0O0O .threedee_model_not_available_img_dir )#line:1547
                    print ('timeout exception end download_threedee_thread')#line:1548
            else :#line:1559
                print ('empty url')#line:1560
                O000O0OOOOOOO0O0O .intense_caverns_img_dir [OO00000000OO0O0O0 ]=os .path .join (O000O0OOOOOOO0O0O .threedee_model_not_available_img_dir )#line:1561
            if IS_3D_TAB_OPEN and not O000O0OOOOOOO0O0O .intense_caverns_thread_started [OO00000000OO0O0O0 ]:#line:1562
                O000O0OOOOOOO0O0O .threedee_text .set ("")#line:1563
                O000O0OOOOOOO0O0O .threedee_image =tk .PhotoImage (file =O000O0OOOOOOO0O0O .intense_caverns_img_dir [OO00000000OO0O0O0 ])#line:1564
                O000O0OOOOOOO0O0O .threedee_model_img =tk .Label (O000O0OOOOOOO0O0O .model_frame ,bg ="white",image =O000O0OOOOOOO0O0O .threedee_image )#line:1565
                O000O0OOOOOOO0O0O .threedee_model_img .grid (row =0 ,column =0 ,sticky ="NEWS",padx =(60 ,60 ))#line:1566
                O000O0OOOOOOO0O0O .model_frame .update_idletasks ()#line:1567
        if IS_3D_TAB_OPEN and O000O0OOOOOOO0O0O .intense_caverns_img_dir [OO00000000OO0O0O0 ]is not None :#line:1568
                O000O0OOOOOOO0O0O .threedee_text .set ("")#line:1569
                O000O0OOOOOOO0O0O .threedee_image =tk .PhotoImage (file =O000O0OOOOOOO0O0O .intense_caverns_img_dir [OO00000000OO0O0O0 ])#line:1570
                O000O0OOOOOOO0O0O .threedee_model_img =tk .Label (O000O0OOOOOOO0O0O .model_frame ,bg ="white",image =O000O0OOOOOOO0O0O .threedee_image )#line:1571
                O000O0OOOOOOO0O0O .threedee_model_img .grid (row =0 ,column =0 ,sticky ="NEWS",padx =(60 ,60 ))#line:1572
                O000O0OOOOOOO0O0O .model_frame .update_idletasks ()#line:1573
    def get_intense_caverns_link (O0O0OO0O0OOOOOOO0 ,O0000O0O0O00O00O0 ):#line:1575
        if O0O0OO0O0OOOOOOO0 .intense_caverns_links [O0000O0O0O00O00O0 ]is None :#line:1576
            O0OOO0OO0O0O0O0O0 =None #line:1577
            OOO0O00O000O00OOO =None #line:1578
            try :#line:1579
                O0OOO0OO0O0O0O0O0 =O0O0OO0O0OOOOOOO0 .data ["results"][O0000O0O0O00O00O0 ]["unipart_id"]#line:1580
                print (O0OOO0OO0O0O0O0O0 )#line:1581
                O00OOO0000O00O000 ={'User-Agent':"Kicad"}#line:1582
                O0O000O0OO0O00OO0 ="https://snapeda.com/api/v1/parts/unipart_3d_viewer_url?unipart_id=%s"%str (O0OOO0OO0O0O0O0O0 )#line:1583
                if sys .version_info [0 ]==3 :#line:1584
                    O0OO000OOOOOOOOOO =urllib .request .Request (O0O000O0OO0O00OO0 ,headers =O00OOO0000O00O000 )#line:1585
                    OO0O0OOO0O0000O0O =urllib .request .urlopen (O0OO000OOOOOOOOOO ,timeout =5 ).read ()#line:1586
                else :#line:1587
                    O0OO000OOOOOOOOOO =urllib2 .Request (O0O000O0OO0O00OO0 ,headers =O00OOO0000O00O000 )#line:1588
                    OO0O0OOO0O0000O0O =urllib2 .urlopen (O0OO000OOOOOOOOOO ,timeout =5 ).read ()#line:1589
                OOO00000O00OO00OO =json .loads (OO0O0OOO0O0000O0O )#line:1590
                OOO0O00O000O00OOO =OOO00000O00OO00OO ["url"]#line:1591
            except :#line:1592
                OOO0O00O000O00OOO =''#line:1593
            if OOO0O00O000O00OOO is not None :#line:1595
                O0O0OO0O0OOOOOOO0 .intense_caverns_links [O0000O0O0O00O00O0 ]=OOO0O00O000O00OOO #line:1596
    def get_component (O00O00000O000OO0O ,OOOO0O00O00OO0OO0 ,O0O00OO0OOO0O0O00 ):#line:1598
        if not O00O00000O000OO0O .side_opened :#line:1609
            for OOOOO000O000O00O0 in O00O00000O000OO0O .manufacturer_names :#line:1610
                OOOOO000O000O00O0 .config (fg ="#999999")#line:1611
            for OO000O00000OO0O0O in O00O00000O000OO0O .manufacturer_labels :#line:1612
                OO000O00000OO0O0O .grid_forget ()#line:1613
            for OO000O00000OO0O0O in O00O00000O000OO0O .available_labels :#line:1614
                OO000O00000OO0O0O .grid_forget ()#line:1615
            O00O00000O000OO0O .canvas_frame .grid_columnconfigure (0 ,weight =0 )#line:1616
            O00O00000O000OO0O .canvas_frame .grid_columnconfigure (1 ,weight =2 )#line:1617
            O00O00000O000OO0O .canvas_frame .grid_columnconfigure (2 ,weight =2 )#line:1618
            O00O00000O000OO0O .canvas_frame .grid_columnconfigure (3 ,weight =0 )#line:1619
            O00O00000O000OO0O .canvas_frame .grid_columnconfigure (4 ,weight =2 )#line:1620
            O00O00000O000OO0O .canvas_frame .grid_columnconfigure (5 ,weight =1 )#line:1621
            O00O00000O000OO0O .canvas_frame .grid_columnconfigure (6 ,weight =3 )#line:1622
        O00O00000O000OO0O .side_opened =True #line:1624
        for O0O0000O0OOOO0OO0 in range (3 ):#line:1625
            O00O00000O000OO0O .dual_frame .grid_columnconfigure (O0O0000O0OOOO0OO0 ,weight =1 ,uniform ="foo")#line:1626
        O00O00000O000OO0O .side_frame =tk .Frame (O00O00000O000OO0O .dual_frame ,bg ="white")#line:1627
        O00O00000O000OO0O .side_frame .grid (row =0 ,column =2 ,columnspan =1 ,sticky ="NEWS")#line:1628
        O00O00000O000OO0O .side_frame .grid_columnconfigure (0 ,weight =1 )#line:1629
        O00O00000O000OO0O .side_frame .grid_rowconfigure (0 ,weight =1 )#line:1630
        O00O00000O000OO0O .details_frame =tk .Frame (O00O00000O000OO0O .side_frame ,bg ="#E1E1E1")#line:1632
        O00O00000O000OO0O .details_frame .grid (row =0 ,column =0 ,sticky ="NEWS",padx =(10 ,0 ),pady =0 )#line:1633
        for O0O0000O0OOOO0OO0 in range (7 ):#line:1634
            O00O00000O000OO0O .details_frame .grid_rowconfigure (O0O0000O0OOOO0OO0 ,weight =1 ,uniform ="foo")#line:1635
        O00O00000O000OO0O .details_frame .grid_columnconfigure (0 ,weight =1 )#line:1636
        O00O00000O000OO0O .load_gif =tk .Label (O00O00000O000OO0O .side_frame ,bg ='white')#line:1638
        O00O00000O000OO0O .load_gif .grid (row =0 ,column =0 ,sticky ="NEWS")#line:1639
        O00O00000O000OO0O .load_gif .lower ()#line:1640
        O00O00000O000OO0O .side_header =tk .Frame (O00O00000O000OO0O .details_frame ,bg ="white")#line:1642
        O00O00000O000OO0O .side_header .grid (row =0 ,column =0 ,rowspan =1 ,sticky ="NEWS",padx =1 ,pady =(1 ,1 ))#line:1643
        O00O00000O000OO0O .side_header .grid_columnconfigure (0 ,weight =1 )#line:1644
        O00O00000O000OO0O .side_header .grid_columnconfigure (1 ,weight =1 )#line:1645
        O00O00000O000OO0O .side_header .grid_rowconfigure (0 ,weight =1 )#line:1646
        O00O00000O000OO0O .details_label =tk .Label (O00O00000O000OO0O .side_header ,bg ="white",text ="Details",font =("Open Sans","8","bold"))#line:1648
        O00O00000O000OO0O .details_label .grid (row =0 ,column =0 ,sticky ="W",padx =(15 ,0 ))#line:1649
        OO0O00O0OOOOO0O00 =O00O00000O000OO0O .data ["results"][O0O00OO0OOO0O0O00 ]#line:1651
        O00O00000O000OO0O .part_number =OO0O00O0OOOOO0O00 ["part_number"]#line:1653
        O00O00000O000OO0O .has_symbol =OO0O00O0OOOOO0O00 ["has_symbol"]#line:1654
        O00O00000O000OO0O .has_footprint =OO0O00O0OOOOO0O00 ["has_footprint"]#line:1655
        O00O00000O000OO0O .has_datasheet =OO0O00O0OOOOO0O00 ["has_datasheet"]#line:1656
        O00O00000O000OO0O .uniqueid =OO0O00O0OOOOO0O00 ["uniqueid"]#line:1657
        O00O00000O000OO0O .manufacturer =OO0O00O0OOOOO0O00 ["manufacturer"]#line:1658
        O00O00000O000OO0O .manufacturer_url =OO0O00O0OOOOO0O00 ["organization_image_100_20"]#line:1659
        try :#line:1661
            OOO000O0000O00OO0 =O00O00000O000OO0O .organization_images [O0O00OO0OOO0O0O00 +1 ]#line:1662
            OOOO0000O0OO00O0O =tk .Label (O00O00000O000OO0O .side_header ,image =OOO000O0000O00OO0 ,bg ="white",font =("Open Sans",9 ))#line:1663
            OOOO0000O0OO00O0O .grid (row =0 ,column =1 ,sticky ="E",padx =(0 ,15 ))#line:1664
        except KeyError :#line:1665
            print ("No Organization Image")#line:1666
            OOOO0000O0OO00O0O =tk .Label (O00O00000O000OO0O .side_header ,text =O00O00000O000OO0O .manufacturer ,bg ="white",font =("Open Sans",9 ))#line:1667
            OOOO0000O0OO00O0O .grid (row =0 ,column =1 ,sticky ="E",padx =(0 ,15 ))#line:1668
        O00O00000O000OO0O .part_details =tk .Frame (O00O00000O000OO0O .details_frame ,bg ="white")#line:1695
        O00O00000O000OO0O .part_details .grid (row =1 ,column =0 ,rowspan =2 ,sticky ="NEWS",padx =1 )#line:1696
        O00O00000O000OO0O .part_details .grid_columnconfigure (0 ,weight =1 )#line:1697
        O00O00000O000OO0O .side_buttons =tk .Frame (O00O00000O000OO0O .part_details ,bg ="white")#line:1698
        O00O00000O000OO0O .side_buttons .grid (row =2 ,column =0 ,padx =(15 ,15 ),sticky ="NEWS")#line:1699
        O00O00000O000OO0O .side_buttons .grid_rowconfigure (0 ,weight =1 )#line:1700
        O00O00000O000OO0O .side_buttons .grid_columnconfigure (0 ,weight =10 ,uniform ="foo")#line:1701
        O00O00000O000OO0O .side_buttons .grid_columnconfigure (1 ,weight =1 ,uniform ="foo")#line:1702
        O00O00000O000OO0O .side_buttons .grid_columnconfigure (2 ,weight =10 ,uniform ="foo")#line:1703
        O00O00000O000OO0O .model_tab_frame =tk .Frame (O00O00000O000OO0O .details_frame ,bg ="white")#line:1705
        O00O00000O000OO0O .model_tab_frame .grid (row =3 ,column =0 ,sticky ="NEWS",padx =1 )#line:1706
        O00O00000O000OO0O .model_tab_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:1707
        O00O00000O000OO0O .model_tab_frame .grid_columnconfigure (1 ,weight =1 ,uniform ="foo")#line:1708
        O00O00000O000OO0O .model_tab_frame .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:1709
        tk .Label (O00O00000O000OO0O .model_tab_frame ,bg ="#DADADA").grid (row =0 ,column =0 ,sticky ="NEWS")#line:1711
        O00O00000O000OO0O .model_2D_underline =tk .Label (O00O00000O000OO0O .model_tab_frame ,bg ="#FF761A")#line:1712
        O00O00000O000OO0O .model_2D_underline .grid (row =0 ,column =0 ,sticky ="NEWS",pady =(1 ,0 ),padx =1 )#line:1713
        O00O00000O000OO0O .model_2D_text =tk .Label (O00O00000O000OO0O .model_tab_frame ,bg ="white",fg ="#FF761A",text ="2D Model",font =("Open Sans",10 ),cursor ="hand2")#line:1714
        O00O00000O000OO0O .model_2D_text .grid (row =0 ,column =0 ,sticky ="NEWS",padx =1 ,pady =(1 ,4 ))#line:1715
        tk .Label (O00O00000O000OO0O .model_tab_frame ,bg ="#DADADA").grid (row =0 ,column =1 ,sticky ="NEWS")#line:1717
        O00O00000O000OO0O .model_3D_text =tk .Label (O00O00000O000OO0O .model_tab_frame ,bg ="#EEEEEE",fg ="#333333",text ="3D Model",font =("Open Sans",10 ),cursor ="hand2")#line:1718
        O00O00000O000OO0O .model_3D_text .grid (row =0 ,column =1 ,sticky ="NEWS",padx =1 ,pady =1 )#line:1719
        O00O00000O000OO0O .side_part_number =tk .Label (O00O00000O000OO0O .part_details ,bg ="white",fg ="#FF761A",font =("Open Sans",12 ),text =OO0O00O0OOOOO0O00 ["part_number"])#line:1721
        O00O00000O000OO0O .side_part_number .grid (row =0 ,column =0 ,sticky ="NWS",padx =(15 ,0 ),pady =(15 ,0 ))#line:1722
        O00O00000O000OO0O .description_message =tk .Message (O00O00000O000OO0O .part_details ,bg ="white",text =OO0O00O0OOOOO0O00 ["short_description"],font =("Open Sans",11 ),cursor ="hand2",justify =tk .LEFT ,anchor ='nw')#line:1727
        O00O00000O000OO0O .description_message .bind ("<Configure>",lambda O0O0OO00000OO0O0O :O0O0OO00000OO0O0O .widget .configure (width =O0O0OO00000OO0O0O .width -8 ))#line:1728
        O00O00000O000OO0O .description_message .grid (row =1 ,column =0 ,columnspan =1 ,sticky ="NEWS",pady =(0 ,10 ),padx =(10 ,10 ))#line:1729
        OOO00O0000O0O0OO0 =tk .PhotoImage (file =O00O00000O000OO0O .download_button_dir )#line:1734
        OOOO0O0O000OO000O =O00O00000O000OO0O .resize (OOO00O0000O0O0OO0 ,90 ,24 )#line:1735
        O00O00000O000OO0O .parent .images .append (OOOO0O0O000OO000O )#line:1736
        O0O000OO0000OOOO0 =tk .PhotoImage (file =O00O00000O000OO0O .view_button_dir )#line:1737
        OOO0OO0OO0000OOO0 =O00O00000O000OO0O .resize (O0O000OO0000OOOO0 ,148 ,39 )#line:1738
        O00O00000O000OO0O .parent .images .append (OOO0OO0OO0000OOO0 )#line:1739
        O00O00000O000OO0O .is_downloading =False #line:1744
        tk .Label (O00O00000O000OO0O .side_buttons ,bg ="#ff761a").grid (row =0 ,column =0 ,sticky ="EW",ipady =7 ,ipadx =72 )#line:1750
        O00O00000O000OO0O .download_button =tk .Label (O00O00000O000OO0O .side_buttons ,bg ="#ff761a",fg ="white",cursor ="hand2",text ="Download",font =("Open Sans",9 ))#line:1751
        O00O00000O000OO0O .download_button .grid (row =0 ,column =0 ,sticky ="EW",padx =(1 ,1 ),ipady =6 ,ipadx =10 )#line:1753
        O00O00000O000OO0O .download_button .bind ("<Button-1>",O00O00000O000OO0O .download_component )#line:1756
        O00O00000O000OO0O .download_button .bind ("<Enter>",lambda O0000OO000O0OO0O0 ,element =O00O00000O000OO0O .download_button :O00O00000O000OO0O .on_button_active (O0000OO000O0OO0O0 ,element ))#line:1757
        O00O00000O000OO0O .download_button .bind ("<Leave>",lambda O0OOO0000000O00OO ,element =O00O00000O000OO0O .download_button :O00O00000O000OO0O .on_button_inactive (O0OOO0000000O00OO ,element ))#line:1758
        tk .Label (O00O00000O000OO0O .side_buttons ,bg ="#ff761a").grid (row =0 ,column =2 ,sticky ="EW",ipady =7 ,ipadx =72 )#line:1762
        O00O00000O000OO0O .view_button =tk .Label (O00O00000O000OO0O .side_buttons ,bg ="#ff761a",fg ="white",cursor ="hand2",text ="Datasheet",font =("Open Sans",9 ))#line:1763
        O00O00000O000OO0O .view_button .grid (row =0 ,column =2 ,sticky ="EW",padx =(1 ,1 ),ipady =6 ,ipadx =10 )#line:1764
        O00O00000O000OO0O .view_button .bind ("<Button-1>",lambda O00OOO000O00000O0 ,url =OO0O00O0OOOOO0O00 ["_links"]["self"]["href"]:O00O00000O000OO0O .view_on_snapeda (url ))#line:1765
        O00O00000O000OO0O .view_button .bind ("<Enter>",lambda OOOO0000O0O0O0O00 ,element =O00O00000O000OO0O .view_button :O00O00000O000OO0O .on_button_active (OOOO0000O0O0O0O00 ,element ))#line:1766
        O00O00000O000OO0O .view_button .bind ("<Leave>",lambda O00OO0OOOO00000O0 ,element =O00O00000O000OO0O .view_button :O00O00000O000OO0O .on_button_inactive (O00OO0OOOO00000O0 ,element ))#line:1767
        O00O00000O000OO0O .symbol_frame =tk .Frame (O00O00000O000OO0O .details_frame ,bg ="white")#line:1795
        O00O00000O000OO0O .symbol_frame .grid (row =4 ,column =0 ,rowspan =3 ,sticky ="NEWS",padx =1 ,pady =(0 ,1 ))#line:1796
        O00O00000O000OO0O .symbol_frame .grid_columnconfigure (0 ,weight =1 )#line:1797
        O00O00000O000OO0O .symbol_frame .grid_rowconfigure (0 ,weight =1 )#line:1798
        O00O00000O000OO0O .model_canvas =tk .Canvas (O00O00000O000OO0O .symbol_frame ,bg ="white")#line:1800
        O00O00000O000OO0O .model_canvas .grid (row =0 ,column =0 ,sticky ="NEWS")#line:1801
        OO00OOO0O000OOO0O =ttk .Style ()#line:1803
        OO00OOO0O000OOO0O .theme_use ('clam')#line:1804
        OO00OOO0O000OOO0O .configure ("snapeda.Vertical.TScrollbar",gripcount =0 ,background ="#FF8330",troughcolor ='#C4C4C4',lightcolor ='#C4C4C4',darkcolor ='#C4C4C4',bordercolor ="#C4C4C4",borderwidth =0 ,relief =tk .FLAT )#line:1805
        OO00OOO0O000OOO0O .map ('snapeda.Vertical.TScrollbar',foreground =[('disabled','#C4C4C4'),('pressed','#FF8330'),('active','#FF8330')],background =[('disabled','#C4C4C4'),('pressed','!focus','#FF8330'),('active','#FF8330')],highlightcolor =[('focus','#C4C4C4'),('!focus','#C4C4C4')],)#line:1813
        OO00OOO0O000OOO0O .layout ('snapeda.Vertical.TScrollbar',[('Vertical.Scrollbar.trough',{'children':[('Vertical.Scrollbar.thumb',{'expand':'1','sticky':'nswe'})],'sticky':'ns'})])#line:1815
        O00O00000O000OO0O .model_scrollbar =ttk .Scrollbar (O00O00000O000OO0O .symbol_frame ,orient ="vertical",command =O00O00000O000OO0O .model_canvas .yview ,style ="snapeda.Vertical.TScrollbar")#line:1816
        O00O00000O000OO0O .model_scrollbar .grid (row =0 ,column =1 ,sticky ='NS')#line:1818
        O00O00000O000OO0O .model_frame =tk .Frame (O00O00000O000OO0O .model_canvas ,bg ="white")#line:1819
        O00O00000O000OO0O .model_frame .bind ("<Configure>",lambda OO00OO0OO0OO00000 :O00O00000O000OO0O .model_canvas .configure (scrollregion =O00O00000O000OO0O .model_canvas .bbox ("all")))#line:1820
        O00O00000O000OO0O .model_canvas .create_window ((0 ,0 ),window =O00O00000O000OO0O .model_frame ,anchor =tk .CENTER )#line:1821
        O00O00000O000OO0O .model_canvas .configure (yscrollcommand =O00O00000O000OO0O .model_scrollbar .set )#line:1822
        O00O00000O000OO0O .threedmodel_medium_image =None #line:1826
        if 'models'in O00O00000O000OO0O .data ["results"][O0O00OO0OOO0O0O00 ]and len (O00O00000O000OO0O .data ["results"][O0O00OO0OOO0O0O00 ]["models"])>0 :#line:1827
            O0000O0O0000OO00O =O00O00000O000OO0O .data ["results"][O0O00OO0OOO0O0O00 ]["models"][0 ]#line:1828
            if '3dmodel_medium'in O0000O0O0000OO00O and 'url'in O0000O0O0000OO00O ['3dmodel_medium']:#line:1829
                print ('downloading 3d')#line:1830
                O00O00000O000OO0O .threedmodel_medium_img_path =O00O00000O000OO0O .download_image (O0000O0O0000OO00O ['3dmodel_medium']['url'])#line:1831
                O00O00000O000OO0O .threedmodel_medium_img =tk .PhotoImage (file =O00O00000O000OO0O .threedmodel_medium_img_path )#line:1832
                O00O00000O000OO0O .threedmodel_medium_image =O00O00000O000OO0O .resize (O00O00000O000OO0O .threedmodel_medium_img ,500 ,500 )#line:1833
                print (O00O00000O000OO0O .download_image (O0000O0O0000OO00O ['3dmodel_medium']['url']))#line:1834
                print ('done')#line:1835
        try :#line:1837
            O00O00000O000OO0O .symbol_im_path =O00O00000O000OO0O .download_image (OO0O00O0OOOOO0O00 ["models"][0 ]["symbol_medium"]["url"])#line:1838
            O0O00000OOOO00OOO =tk .PhotoImage (file =O00O00000O000OO0O .symbol_im_path )#line:1839
            O00O00000O000OO0O .symbol_image =O00O00000O000OO0O .resize (O0O00000OOOO00OOO ,210 ,210 )#line:1840
            O00O00000O000OO0O .symbol_view =tk .Label (O00O00000O000OO0O .model_frame ,bg ="white",image =O00O00000O000OO0O .symbol_image )#line:1842
            O00O00000O000OO0O .symbol_view .grid (row =0 ,column =0 ,sticky ="NEWS",padx =(65 ,65 ))#line:1843
            O00O00000O000OO0O .has_model =True #line:1844
        except KeyError :#line:1845
            O00O00000O000OO0O .symbol_view =tk .Frame (O00O00000O000OO0O .model_frame ,bg ="white")#line:1846
            O00O00000O000OO0O .symbol_view .columnconfigure (0 ,weight =1 ,uniform ='foo')#line:1847
            O00O00000O000OO0O .symbol_view .grid (row =0 ,column =0 ,sticky ='NEWS',padx =(60 ,60 ))#line:1850
            O00O00000O000OO0O .ghost_2D_im =tk .PhotoImage (file =O00O00000O000OO0O .not_available_img_dir )#line:1851
            tk .Label (O00O00000O000OO0O .symbol_view ,bg ="white",image =O00O00000O000OO0O .ghost_2D_im ).grid (row =0 ,column =0 ,sticky ="NEWS")#line:1854
            O00O00000O000OO0O .request_button_img =tk .PhotoImage (file =O00O00000O000OO0O .request_now_button_img_dir )#line:1855
            O00O00000O000OO0O .request_button =tk .Label (O00O00000O000OO0O .symbol_view ,bg ="white",image =O00O00000O000OO0O .request_button_img ,cursor ="hand2")#line:1857
            O00O00000O000OO0O .request_button .grid (row =1 ,column =0 ,sticky ="NEWS",pady =(0 ,30 ))#line:1858
            O00O00000O000OO0O .request_button .bind ('<Button-1>',O00O00000O000OO0O .request_now_button_callback )#line:1859
            O00O00000O000OO0O .has_model =False #line:1860
        O00O00000O000OO0O .tab_view =O00O00000O000OO0O .symbol_view #line:1862
        try :#line:1864
            OO00OOOOOOO00OOO0 =O00O00000O000OO0O .download_image (OO0O00O0OOOOO0O00 ["models"][0 ]["package_medium"]["url"])#line:1865
            O000O000O0OO000OO =tk .PhotoImage (file =OO00OOOOOOO00OOO0 )#line:1866
            O00O00000O000OO0O .package_image =O00O00000O000OO0O .resize (O000O000O0OO000OO ,150 ,150 )#line:1867
            OOO0OO00OOO00O0O0 =tk .Label (O00O00000O000OO0O .model_frame ,bg ="white",image =O00O00000O000OO0O .package_image )#line:1869
            OOO0OO00OOO00O0O0 .grid (row =1 ,column =0 ,sticky ="NEWS")#line:1870
            O00O00000O000OO0O .has_package =True #line:1871
        except KeyError :#line:1872
            OOO0OO00OOO00O0O0 =tk .Frame (O00O00000O000OO0O .model_frame ,bg ="white")#line:1873
            OOO0OO00OOO00O0O0 .columnconfigure (0 ,weight =1 ,uniform ='foo')#line:1874
            OOO0OO00OOO00O0O0 .rowconfigure (0 ,weight =2 ,uniform ='foo')#line:1875
            OOO0OO00OOO00O0O0 .rowconfigure (0 ,weight =1 ,uniform ='foo')#line:1876
            OOO0OO00OOO00O0O0 .grid (row =1 ,column =0 ,sticky ='NEWS')#line:1877
            O00O00000O000OO0O .ghost_im =tk .PhotoImage (file =O00O00000O000OO0O .avatar_image_dir )#line:1878
            tk .Label (OOO0OO00OOO00O0O0 ,bg ="white",image =O00O00000O000OO0O .ghost_im ).grid (row =0 ,column =0 ,sticky ="NEWS")#line:1881
            tk .Label (OOO0OO00OOO00O0O0 ,bg ="white",text ='No Package',font =("Open Sans",11 )).grid (row =1 ,column =0 ,sticky ="NEWS",pady =(0 ,15 ))#line:1882
            print ("No package")#line:1883
            O00O00000O000OO0O .has_package =False #line:1884
        O00O00000O000OO0O .model_2D_text .bind ('<Button-1>',lambda O00OOO000OO0000OO ,index =O0O00OO0OOO0O0O00 :O00O00000O000OO0O .model_2D_callback (O00OOO000OO0000OO ,index ))#line:1886
        O00O00000O000OO0O .model_3D_text .bind ('<Button-1>',lambda OOOOO00O0OO00OO00 ,index =O0O00OO0OOO0O0O00 :O00O00000O000OO0O .model_3D_callback (OOOOO00O0OO00OO00 ,index ))#line:1887
        O00O00000O000OO0O .is_loading =False #line:1889
        O00O00000O000OO0O .description_message .update_idletasks ()#line:1892
        O00O00000O000OO0O .part_details .update_idletasks ()#line:1893
        O00O00000O000OO0O .details_frame .lift ()#line:1894
    def canvas_frame_wh (O0OOO000O0O0O0O0O ,OO0O000OOOOO0OO00 ):#line:1896
        OO000O000OO000000 =O0OOO000O0O0O0O0O .canvas .winfo_width ()#line:1897
        print ("break3")#line:1898
        O0OOO000O0O0O0O0O .canvas .itemconfigure ("inner_frame",width =OO000O000OO000000 -4 )#line:1899
    def initialize_user_interface (OO0OO00000OOO0O0O ):#line:1901
        if OO0OO00000OOO0O0O .is_windows :#line:1902
            OO0OO00000OOO0O0O .parent .iconbitmap (OO0OO00000OOO0O0O .icon_bitmap_dir )#line:1903
        OO0OO00000OOO0O0O .parent .title ("SnapEDA v"+OO0OO00000OOO0O0O .parent .version )#line:1904
        OO0OO00000OOO0O0O .parent .geometry ("1150x828")#line:1905
        OO0OO00000OOO0O0O .parent .minsize (width =1150 ,height =828 )#line:1906
        OO0OO00000OOO0O0O .light_gray ="#FAFAFA"#line:1907
        OO0OO00000OOO0O0O .medium_gray ="#E1E1E1"#line:1908
        OO0OO00000OOO0O0O .dark_gray ="#696969"#line:1909
        OO0OO00000OOO0O0O .parent .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:1910
        OO0OO00000OOO0O0O .parent .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:1911
        OO0OO00000OOO0O0O .parent_container =tk .Frame (OO0OO00000OOO0O0O .parent ,bg =OO0OO00000OOO0O0O .dark_gray )#line:1912
        OO0OO00000OOO0O0O .parent_container .grid (row =0 ,column =0 ,sticky ="NEWS")#line:1913
        for OOO0000O00O0O000O in range (6 ):#line:1914
            OO0OO00000OOO0O0O .parent_container .grid_columnconfigure (OOO0000O00O0O000O ,weight =1 ,uniform ="foo")#line:1915
        OO0OO00000OOO0O0O .parent_container .grid_rowconfigure (0 ,weight =1 )#line:1916
        OO0OO00000OOO0O0O .main_frame =tk .Frame (OO0OO00000OOO0O0O .parent_container ,bg ="white")#line:1917
        OO0OO00000OOO0O0O .main_frame .grid (row =0 ,column =0 ,columnspan =6 ,sticky ="NEWS")#line:1918
        OO0OO00000OOO0O0O .main_frame .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:1922
        for OOO0000O00O0O000O in range (6 ):#line:1923
            OO0OO00000OOO0O0O .main_frame .grid_rowconfigure (OOO0000O00O0O000O ,weight =1 ,uniform ="foo")#line:1924
        OO0OO00000OOO0O0O .parent .images =[]#line:1925
        OO0OO00000OOO0O0O .parent .default_images =[]#line:1926
        OO0OO00000OOO0O0O .current_page =1 #line:1927
        OO0OO00000OOO0O0O .max_page =1 #line:1928
        OO0OO00000OOO0O0O .top_wh =75 #line:1929
        OO0OO00000OOO0O0O .pages =[]#line:1930
        OO0OO00000OOO0O0O .side_opened =False #line:1931
        OO0OO00000OOO0O0O .search_frame =tk .Frame (OO0OO00000OOO0O0O .main_frame ,bg ="white")#line:1981
        OO0OO00000OOO0O0O .search_frame .grid (row =0 ,column =0 ,columnspan =1 ,sticky ="EW",padx =(18 ,0 ))#line:1982
        for OOO0000O00O0O000O in range (3 ):#line:1983
            OO0OO00000OOO0O0O .search_frame .grid_columnconfigure (OOO0000O00O0O000O +1 ,weight =1 ,uniform ="foo")#line:1984
        OO0OO00000OOO0O0O .search_frame .grid_rowconfigure (0 ,weight =0 )#line:1985
        OO0OO00000OOO0O0O .home_menu_img =tk .PhotoImage (file =OO0OO00000OOO0O0O .home_menu_img_dir )#line:1992
        OO0OO00000OOO0O0O .home_button =tk .Label (OO0OO00000OOO0O0O .search_frame ,image =OO0OO00000OOO0O0O .home_menu_img ,fg ="#FF761B",bg ="white",text ="HOME",cursor ="hand2",font =("Open Sans","8","bold","underline"))#line:1993
        OO0OO00000OOO0O0O .home_button .grid (row =0 ,column =0 ,padx =(0 ,15 ),sticky ="W")#line:1994
        OO0OO00000OOO0O0O .home_button .bind ("<Button-1>",OO0OO00000OOO0O0O .home_callback )#line:1995
        O000O000OOOOOOO00 =tk .Frame (OO0OO00000OOO0O0O .search_frame ,bg ="white")#line:1997
        O000O000OOOOOOO00 .grid (row =0 ,column =1 ,columnspan =1 ,sticky ="NEWS",pady =2 ,padx =(0 ,0 ))#line:1998
        O000O000OOOOOOO00 .grid_columnconfigure (0 ,weight =1 )#line:1999
        O000O000OOOOOOO00 .grid_rowconfigure (0 ,weight =1 )#line:2000
        tk .Label (O000O000OOOOOOO00 ,bg ="#E1E1E1").grid (row =0 ,column =0 ,sticky ="NEWS",padx =(0 ,0 ),pady =(0 ,0 ))#line:2005
        tk .Label (O000O000OOOOOOO00 ,bg ="white").grid (row =0 ,column =0 ,sticky ="NEWS",padx =(1 ,0 ),pady =(1 ,1 ))#line:2006
        OO0OO00000OOO0O0O .search_entry =tk .Entry (O000O000OOOOOOO00 ,fg ="#696969",bg ="white",font =("Open Sans",9 ),borderwidth =0 ,highlightthickness =0 )#line:2008
        OO0OO00000OOO0O0O .search_entry .insert (0 ,OO0OO00000OOO0O0O .parent .search_datum )#line:2009
        OO0OO00000OOO0O0O .search_entry .grid (row =0 ,column =0 ,sticky ="NEWS",padx =(25 ,0 ),pady =(1 ,1 ))#line:2010
        OO0OOO0000O000O00 =tk .PhotoImage (file =OO0OO00000OOO0O0O .search_button_image_dir )#line:2012
        OOOO000O0000O00O0 =OO0OO00000OOO0O0O .resize (OO0OOO0000O000O00 ,73 ,55 )#line:2013
        OO0OO00000OOO0O0O .parent .images .append (OOOO000O0000O00O0 )#line:2014
        OO0OO00000OOO0O0O .search_button =tk .Label (OO0OO00000OOO0O0O .search_frame ,bg ="white",text ="",cursor ="hand2",image =OOOO000O0000O00O0 )#line:2015
        OO0OO00000OOO0O0O .is_searching =False #line:2016
        OO0OO00000OOO0O0O .search_button .bind ("<Button-1>",OO0OO00000OOO0O0O .search_data )#line:2017
        OO0OO00000OOO0O0O .search_entry .bind ('<Return>',OO0OO00000OOO0O0O .search_data )#line:2018
        OO0OO00000OOO0O0O .search_entry .bind ('<Button-3>',OO0OO00000OOO0O0O .show_copy_paste_option )#line:2019
        OO0OO00000OOO0O0O .search_button .grid (row =0 ,column =2 ,sticky ="W")#line:2020
        OO0OO00000OOO0O0O .menu_container =tk .Frame (OO0OO00000OOO0O0O .search_frame ,bg ="white")#line:2023
        OO0OO00000OOO0O0O .menu_container .grid (row =0 ,column =3 ,columnspan =3 ,sticky ="E",padx =(0 ,18 ))#line:2024
        OO0OO00000OOO0O0O .menu_container .grid_rowconfigure (0 ,weight =1 )#line:2025
        OO0OO00000OOO0O0O .how_it_works_menu_img =tk .PhotoImage (file =OO0OO00000OOO0O0O .how_it_works_menu_img_dir )#line:2036
        OO0OO00000OOO0O0O .how_it_works_button =tk .Label (OO0OO00000OOO0O0O .menu_container ,image =OO0OO00000OOO0O0O .how_it_works_menu_img ,fg ="#FF761B",bg ="white",text ="How it works",cursor ="hand2",font =("Open Sans","8","bold","underline"))#line:2037
        OO0OO00000OOO0O0O .how_it_works_button .grid (row =0 ,column =0 ,padx =(0 ,15 ),sticky ="W")#line:2038
        OO0OO00000OOO0O0O .how_it_works_button .bind ("<Button-1>",OO0OO00000OOO0O0O .setting_callback )#line:2039
        OO0OO00000OOO0O0O .update_menu_img =tk .PhotoImage (file =OO0OO00000OOO0O0O .update_menu_img_dir )#line:2041
        OO0OO00000OOO0O0O .update_button =tk .Label (OO0OO00000OOO0O0O .menu_container ,image =OO0OO00000OOO0O0O .update_menu_img ,fg ="#FF761B",bg ="white",text ="Update",cursor ="hand2",font =("Open Sans","8","bold","underline"))#line:2042
        OO0OO00000OOO0O0O .update_button .grid (row =0 ,column =1 ,padx =(0 ,15 ),sticky ="W")#line:2043
        OO0OO00000OOO0O0O .update_button .bind ("<Button-1>",OO0OO00000OOO0O0O .update_callback )#line:2044
        OO0OO00000OOO0O0O .info_menu_img =tk .PhotoImage (file =OO0OO00000OOO0O0O .info_menu_img_dir )#line:2046
        OO0OO00000OOO0O0O .help_me_button =tk .Label (OO0OO00000OOO0O0O .menu_container ,image =OO0OO00000OOO0O0O .info_menu_img ,fg ="#FF761B",bg ="white",text ="Help Me",cursor ="hand2",font =("Open Sans","8","bold","underline"))#line:2047
        OO0OO00000OOO0O0O .help_me_button .grid (row =0 ,column =2 ,padx =(0 ,15 ),sticky ="W")#line:2048
        OO0OO00000OOO0O0O .help_me_button .bind ("<Button-1>",OO0OO00000OOO0O0O .how_it_works_callback )#line:2049
        OO0OO00000OOO0O0O .logout_menu_img =tk .PhotoImage (file =OO0OO00000OOO0O0O .logout_menu_img_dir )#line:2051
        OO0OO00000OOO0O0O .logout_button =tk .Label (OO0OO00000OOO0O0O .menu_container ,image =OO0OO00000OOO0O0O .logout_menu_img ,fg ="#FF761B",bg ="white",text ="Logout",cursor ="hand2",font =("Open Sans","8","bold","underline"))#line:2052
        OO0OO00000OOO0O0O .logout_button .grid (row =0 ,column =3 ,padx =(0 ,15 ))#line:2053
        OO0OO00000OOO0O0O .logout_button .bind ("<Button-1>",OO0OO00000OOO0O0O .logout_callback )#line:2054
        OO0OO00000OOO0O0O .table_frame =tk .Frame (OO0OO00000OOO0O0O .main_frame ,bg ="white")#line:2056
        OO0OO00000OOO0O0O .table_frame .grid (row =1 ,column =0 ,rowspan =5 ,columnspan =1 ,padx =19 ,pady =(0 ,13 ),sticky ="NEWS")#line:2057
        for OOO0000O00O0O000O in range (7 ):#line:2064
            OO0OO00000OOO0O0O .table_frame .grid_rowconfigure (OOO0000O00O0O000O ,weight =1 ,uniform ="foo")#line:2065
        OO0OO00000OOO0O0O .table_frame .grid_columnconfigure (0 ,weight =1 )#line:2066
        OO0OO00000OOO0O0O .table_frame .grid_columnconfigure (1 ,weight =1 )#line:2067
        OO0OO00000OOO0O0O .dual_frame =tk .Frame (OO0OO00000OOO0O0O .table_frame ,bg ="#E1E1E1")#line:2069
        OO0OO00000OOO0O0O .dual_frame .grid (row =0 ,column =0 ,columnspan =2 ,rowspan =6 ,sticky ="NEWS")#line:2070
        OO0OO00000OOO0O0O .dual_frame .grid_rowconfigure (0 ,weight =1 )#line:2071
        for OOO0000O00O0O000O in range (2 ):#line:2072
            OO0OO00000OOO0O0O .dual_frame .grid_columnconfigure (OOO0000O00O0O000O ,weight =1 ,uniform ="foo")#line:2073
        OO0OO00000OOO0O0O .results_frame =tk .Frame (OO0OO00000OOO0O0O .dual_frame ,bg ="white")#line:2074
        OO0OO00000OOO0O0O .results_frame .grid (row =0 ,column =0 ,columnspan =2 ,sticky ="NEWS",pady =(0 ,1 ))#line:2075
        OO0OO00000OOO0O0O .results_frame .grid_columnconfigure (0 ,weight =1 )#line:2076
        OO0OO00000OOO0O0O .results_frame .grid_rowconfigure (0 ,weight =1 )#line:2078
        OO0OO00000OOO0O0O .results_frame .update ()#line:2079
        OO0OO00000OOO0O0O .canvas =tk .Canvas (OO0OO00000OOO0O0O .results_frame ,bg ="white")#line:2080
        OO0OO00000OOO0O0O .canvas .grid (row =0 ,column =0 ,sticky ="NEWS")#line:2081
        O00OOO0O00OOOO00O =ttk .Style ()#line:2088
        O00OOO0O00OOOO00O .theme_use ('clam')#line:2089
        O00OOO0O00OOOO00O .configure ("snapeda.Vertical.TScrollbar",gripcount =0 ,background ="#FF8330",troughcolor ='#C4C4C4',lightcolor ='#C4C4C4',darkcolor ='#C4C4C4',bordercolor ="#C4C4C4",borderwidth =0 ,relief =tk .FLAT )#line:2090
        O00OOO0O00OOOO00O .map ('snapeda.Vertical.TScrollbar',foreground =[('disabled','#C4C4C4'),('pressed','#FF8330'),('active','#FF8330')],background =[('disabled','#C4C4C4'),('pressed','!focus','#FF8330'),('active','#FF8330')],highlightcolor =[('focus','#C4C4C4'),('!focus','#C4C4C4')],)#line:2098
        O00OOO0O00OOOO00O .layout ('snapeda.Vertical.TScrollbar',[('Vertical.Scrollbar.trough',{'children':[('Vertical.Scrollbar.thumb',{'expand':'1','sticky':'nswe'})],'sticky':'ns'})])#line:2100
        OO0OO00000OOO0O0O .vsb =ttk .Scrollbar (OO0OO00000OOO0O0O .results_frame ,orient ="vertical",command =OO0OO00000OOO0O0O .canvas .yview ,style ="snapeda.Vertical.TScrollbar")#line:2101
        OO0OO00000OOO0O0O .vsb .grid (row =0 ,column =1 ,sticky ='NS')#line:2102
        OO0OO00000OOO0O0O .canvas .configure (yscrollcommand =OO0OO00000OOO0O0O .vsb .set )#line:2103
        OO0OO00000OOO0O0O .canvas .configure (width =OO0OO00000OOO0O0O .results_frame .winfo_width ()/16 )#line:2104
        OO0OO00000OOO0O0O .canvas_frame =tk .Frame (OO0OO00000OOO0O0O .canvas ,bg ="white")#line:2106
        OO0OO00000OOO0O0O .canvas .create_window ((0 ,0 ),window =OO0OO00000OOO0O0O .canvas_frame ,anchor ='nw',tag ="inner_frame")#line:2112
        OO0OO00000OOO0O0O .canvas .update_idletasks ()#line:2113
        OO0OO00000OOO0O0O .canvas_frame .update_idletasks ()#line:2114
        OO0OO00000OOO0O0O .canvas .config (scrollregion =OO0OO00000OOO0O0O .canvas .bbox ("all"))#line:2115
        OO0OO00000OOO0O0O .canvas .bind ('<Configure>',OO0OO00000OOO0O0O .canvas_frame_wh )#line:2118
        OO0OO00000OOO0O0O .canvas .config (scrollregion =OO0OO00000OOO0O0O .canvas .bbox ("all"))#line:2121
        OO0OO00000OOO0O0O .pages_frame =tk .Frame (OO0OO00000OOO0O0O .table_frame ,bg ="#E1E1E1")#line:2122
        OO0OO00000OOO0O0O .pages_frame .grid (row =6 ,column =0 ,sticky ="W",padx =(0 ,0 ))#line:2123
        OO0OO00000OOO0O0O .frames =[tk .PhotoImage (file =os .path .join (OO0OO00000OOO0O0O .loading_image_dir ),format ='gif -index %i'%(O0O0O0OOO00OO0O00 ))for O0O0O0OOO00OO0O00 in range (31 )]#line:2126
        OO0OO00000OOO0O0O .search_gif =tk .Label (OO0OO00000OOO0O0O .results_frame ,bg ='white')#line:2127
        OO0OO00000OOO0O0O .search_gif .grid (row =0 ,column =0 ,sticky ="NEWS")#line:2128
        OO0OO00000OOO0O0O .search_gif .lower ()#line:2129
        OO0OO00000OOO0O0O .vsb .update_idletasks ()#line:2131
        O00OOOOOOO00OO0O0 =tk .PhotoImage (file =OO0OO00000OOO0O0O .powered_image_dir )#line:2132
        OO0OO00000OOO0O0O .powered_image =OO0OO00000OOO0O0O .resize (O00OOOOOOO00OO0O0 ,150 ,33 )#line:2133
        OO0OO00000OOO0O0O .parent .images .append (OO0OO00000OOO0O0O .powered_image )#line:2134
        OO0OO00000OOO0O0O .snapeda_powered =tk .Label (OO0OO00000OOO0O0O .table_frame ,image =OO0OO00000OOO0O0O .powered_image ,bg ="white")#line:2135
        OO0OO00000OOO0O0O .snapeda_powered .grid (row =6 ,column =1 ,sticky ="E",padx =(0 ,OO0OO00000OOO0O0O .vsb .winfo_width ()))#line:2136
        OO0OO00000OOO0O0O .search_data (OO0OO00000OOO0O0O )#line:2137
    def resize (OOO0OO0OOOO00OOOO ,OO0O00OOO00O0000O ,OO0O0OO0OO00OO000 ,O0O00O0O0OOOO0O0O ):#line:2139
        ""#line:2143
        if sys .version_info [0 ]==3 :#line:2144
            OO0000O0OO0O0O000 =OO0O00OOO00O0000O .width ()#line:2145
            OO000O00O00OOO0OO =OO0O00OOO00O0000O .height ()#line:2146
            OOO00O00OO0OO0OO0 =max (OO0000O0OO0O0O000 ,OO000O00O00OOO0OO )#line:2147
            O0O0OO0OO000O00O0 =max (OO0O0OO0OO00OO000 ,O0O00O0O0OOOO0O0O )#line:2148
            if OOO00O00OO0OO0OO0 >O0O0OO0OO000O00O0 :#line:2149
                return OO0O00OOO00O0000O .subsample (int (OOO00O00OO0OO0OO0 /O0O0OO0OO000O00O0 ))#line:2150
            else :#line:2151
                return OO0O00OOO00O0000O .zoom (int (O0O0OO0OO000O00O0 /OOO00O00OO0OO0OO0 ))#line:2152
        else :#line:2153
            OO0000O0OO0O0O000 =OO0O00OOO00O0000O .width ()#line:2154
            OO000O00O00OOO0OO =OO0O00OOO00O0000O .height ()#line:2155
            OOO00O00OO0OO0OO0 =max (OO0000O0OO0O0O000 ,OO000O00O00OOO0OO )#line:2156
            O0O0OO0OO000O00O0 =max (OO0O0OO0OO00OO000 ,O0O00O0O0OOOO0O0O )#line:2157
            if OOO00O00OO0OO0OO0 >O0O0OO0OO000O00O0 :#line:2158
                return OO0O00OOO00O0000O .subsample (OOO00O00OO0OO0OO0 /O0O0OO0OO000O00O0 )#line:2159
            else :#line:2160
                return OO0O00OOO00O0000O .zoom (O0O0OO0OO000O00O0 /OOO00O00OO0OO0OO0 )#line:2161
    def image_return (OO00OO0O0OO00O0O0 ,O0000OO00O0OOOOOO ):#line:2163
        return O0000OO00O0OOOOOO #line:2164
    def download_image (OOO0OOO0O00O00OOO ,OO0OO00OO0O0OO00O ):#line:2166
        OO0O0OOOO00O00000 =OO0OO00OO0O0OO00O [OO0OO00OO0O0OO00O .rfind ('/')+1 :]#line:2168
        OO0OOOO0OO0O0O00O =os .path .join (OOO0OOO0O00O00OOO .appdata_dir ,OO0O0OOOO00O00000 )#line:2169
        O0O0000O000OOO000 =OO0OOOO0OO0O0O00O [:-3 ]+"png"#line:2170
        OO0OO0OOO00OO000O =threading .Timer (2 ,OOO0OOO0O00O00OOO .image_return ,args =(O0O0000O000OOO000 ,))#line:2171
        OO0OO0OOO00OO000O .start ()#line:2172
        if not os .path .exists (O0O0000O000OOO000 )and not OOO0OOO0O00O00OOO .is_mac :#line:2173
            if OOO0OOO0O00O00OOO .is_windows :#line:2174
                OOO0000O0000OO0O0 =os .path .join (os .path .dirname (__file__ ),"imagemagick","convert")#line:2175
                subprocess .check_call ([OOO0000O0000OO0O0 ,OO0OO00OO0O0OO00O .replace ("https","http"),O0O0000O000OOO000 ],shell =True )#line:2176
            else :#line:2177
                subprocess .call ("convert "+OO0OO00OO0O0OO00O .replace ("https","http")+" "+O0O0000O000OOO000 ,shell =True )#line:2178
        if OOO0OOO0O00O00OOO .is_mac :#line:2179
            if not os .path .exists (O0O0000O000OOO000 ):#line:2180
                with open (OO0OOOO0OO0O0O00O ,"wb")as OO0OOOO000O0O0O00 :#line:2181
                    if sys .version_info [0 ]==3 :#line:2182
                        OO0OO000O0000OOOO =urllib .request .urlopen (OO0OO00OO0O0OO00O ).read ()#line:2183
                    else :#line:2184
                        OO0OO000O0000OOOO =urllib2 .urlopen (OO0OO00OO0O0OO00O ).read ()#line:2185
                    OO0OOOO000O0O0O00 .write (OO0OO000O0000OOOO )#line:2186
                    OO0OOOO000O0O0O00 .close ()#line:2187
                    subprocess .check_call (["sips","-s","format","gif","%s"%OO0OOOO0OO0O0O00O ,"--out","%s"%O0O0000O000OOO000 ],shell =True )#line:2188
        return O0O0000O000OOO000 #line:2189
    def update_search (O00O0O0O0OOO0OO00 ,OOO0OOO0000O00OOO ):#line:2191
        OOO0OOOO0OOOO0O00 =O00O0O0O0OOO0OO00 .frames [OOO0OOO0000O00OOO ]#line:2192
        OOO0OOO0000O00OOO +=1 #line:2193
        if OOO0OOO0000O00OOO ==30 :#line:2194
            OOO0OOO0000O00OOO =0 #line:2195
        O00O0O0O0OOO0OO00 .search_gif .config (image =OOO0OOOO0OOOO0O00 )#line:2196
        O00O0O0O0OOO0OO00 .search_after =O00O0O0O0OOO0OO00 .parent .after (30 ,O00O0O0O0OOO0OO00 .update_search ,OOO0OOO0000O00OOO )#line:2197
    def update_load (OOO00O0OOOO0OOO0O ,OO0O0OOOOO00O00O0 ):#line:2199
        O00OOOO00O0OOO00O =OOO00O0OOOO0OOO0O .frames [OO0O0OOOOO00O00O0 ]#line:2200
        OO0O0OOOOO00O00O0 +=1 #line:2201
        if OO0O0OOOOO00O00O0 ==30 :#line:2202
            OO0O0OOOOO00O00O0 =0 #line:2203
        OOO00O0OOOO0OOO0O .load_gif .config (image =O00OOOO00O0OOO00O )#line:2204
        OOO00O0OOOO0OOO0O .load_after =OOO00O0OOOO0OOO0O .parent .after (30 ,OOO00O0OOOO0OOO0O .update_load ,OO0O0OOOOO00O00O0 )#line:2205
    def mouse_wheel_callback (O000OOOOO00O00OO0 ,O0OOOOO00O00O00OO ):#line:2207
        O000OOOOO00O00OO0 .canvas .yview_scroll (int (-1 *(O0OOOOO00O00O00OO .delta /120 )),"units")#line:2208
    def search_data (O0000O00OOOOOO00O ,OOOOOOO0OO0O0OOOO ,current_page =1 ):#line:2211
        if not O0000O00OOOOOO00O .is_searching and len (O0000O00OOOOOO00O .search_entry .get ())>0 :#line:2212
            O0000O00OOOOOO00O .is_searching =True #line:2213
            O0000O00OOOOOO00O .search_button .config (state ="disabled")#line:2214
            O0000O00OOOOOO00O .search_entry .config (state ="disabled",disabledbackground ="white")#line:2215
            print ("searched page: %d"%current_page )#line:2218
            O0000O00OOOOOO00O .search_thread =threading .Thread (target =O0000O00OOOOOO00O .insert_data ,kwargs ={'current_page':current_page })#line:2219
            O0000O00OOOOOO00O .search_thread .setDaemon (True )#line:2220
            O0000O00OOOOOO00O .search_thread .start ()#line:2221
            O0000O00OOOOOO00O .table_frame .lower ()#line:2222
            O0000O00OOOOOO00O .pages_frame .destroy ()#line:2223
            O0000O00OOOOOO00O .search_gif .lift ()#line:2224
            O0000O00OOOOOO00O .search_after =O0000O00OOOOOO00O .parent .after (0 ,O0000O00OOOOOO00O .update_search ,0 )#line:2225
    def select_all_option (OOOO00OOOOOOO00OO ):#line:2227
        OOOO00OOOOOOO00OO .search_entry .focus ()#line:2228
        OOOO00OOOOOOO00OO .search_entry .index (tk .INSERT )#line:2229
        O0OO000O0O0OO000O =OOOO00OOOOOOO00OO .search_entry .selection_range (0 ,tk .END )#line:2230
    def cut_option (O0O0OO0OOOO000O00 ):#line:2232
        if O0O0OO0OOOO000O00 .search_entry .selection_present ():#line:2233
            O0000OO0OO000O000 =O0O0OO0OOOO000O00 .search_entry .selection_get ()#line:2234
            O0O0OO0OOOO000O00 .search_entry .delete ("sel.first","sel.last")#line:2235
            O0O0OO0OOOO000O00 .parent .clipboard_clear ()#line:2237
            O0O0OO0OOOO000O00 .parent .clipboard_append (O0000OO0OO000O000 )#line:2238
    def copy_option (O0OOOOOO0000O000O ):#line:2240
        if O0OOOOOO0000O000O .search_entry .selection_present ():#line:2241
            OOO0O0O00O00OO000 =O0OOOOOO0000O000O .search_entry .selection_get ()#line:2242
            O0OOOOOO0000O000O .parent .clipboard_clear ()#line:2244
            O0OOOOOO0000O000O .parent .clipboard_append (OOO0O0O00O00OO000 )#line:2245
    def paste_option (OOOO00000OOO00000 ):#line:2247
        OO00O0O0O00OO0OOO =OOOO00000OOO00000 .parent .clipboard_get ()#line:2248
        if OOOO00000OOO00000 .search_entry .selection_present ():#line:2249
            OOOO00000OOO00000 .search_entry .delete ("sel.first","sel.last")#line:2250
        OOOO00000OOO00000 .search_entry .insert ('insert',OO00O0O0O00OO0OOO )#line:2251
    def show_copy_paste_option (OOOO00000O000O0OO ,O00OO00O0O0OOO0O0 ):#line:2253
        OO0O00OOO00O0O0O0 =tk .Menu (OOOO00000O000O0OO .parent ,tearoff =0 )#line:2254
        OO0O00OOO00O0O0O0 .add_command (label ="Select All",command =OOOO00000O000O0OO .select_all_option )#line:2255
        OO0O00OOO00O0O0O0 .add_command (label ="Cut",command =OOOO00000O000O0OO .cut_option )#line:2256
        OO0O00OOO00O0O0O0 .add_command (label ="Copy",command =OOOO00000O000O0OO .copy_option )#line:2257
        OO0O00OOO00O0O0O0 .add_command (label ="Paste",command =OOOO00000O000O0OO .paste_option )#line:2258
        try :#line:2262
            OO0O00OOO00O0O0O0 .tk_popup (O00OO00O0O0OOO0O0 .x_root ,O00OO00O0O0OOO0O0 .y_root )#line:2263
        finally :#line:2264
            OO0O00OOO00O0O0O0 .grab_release ()#line:2265
    def request_callback (OO0000000O0O00OO0 ,O00000OO0O0OOOOO0 ):#line:2267
        webbrowser .open ("https://www.cognitoforms.com/SnapEDA/PartRequestForm",new =2 )#line:2268
    def insert_data (O0000O0000OO0O00O ,current_page =1 ):#line:2270
        ""#line:2273
        O0000O0000OO0O00O .intense_caverns_links =[]#line:2275
        O0000O0000OO0O00O .intense_caverns_img_dir =[]#line:2276
        O0000O0000OO0O00O .intense_caverns_thread_started =[]#line:2277
        O00OOO0O0OO000000 =os .path .join (O0000O0000OO0O00O .appdata_dir ,"info.json")#line:2280
        with open (O00OOO0O0OO000000 )as OO000O0OOOOO00000 :#line:2281
            OOOOOOOOOO0O000O0 =json .load (OO000O0OOOOO00000 )#line:2282
        OO000O000OO0000O0 =OOOOOOOOOO0O000O0 ['username']#line:2283
        O0000O0000OO0O00O .token ="XbBKBKXLpgRYz96cfSaQDpToMmHFg6jH"#line:2285
        O0O000OO00O00OO0O ={'User-Agent':"Kicad"}#line:2286
        OO000OO00000O00O0 =str (O0000O0000OO0O00O .search_entry .get ()).replace (" ","%20")#line:2287
        O000O00000OOO00O0 ="https://www.snapeda.com/api/v1/parts/search?q=%s&token=%s&page=%s&ref=%s&username=%s&plugin=%s"%(OO000OO00000O00O0 ,O0000O0000OO0O00O .token ,str (current_page ),"kicad-plugin",OO000O000OO0000O0 ,'kicad')#line:2289
        print ('Search URL: '+O000O00000OOO00O0 )#line:2290
        try :#line:2291
            O0000O0000OO0O00O .message_frame .destroy ()#line:2292
        except :#line:2293
            pass #line:2294
        try :#line:2295
            if sys .version_info [0 ]==3 :#line:2296
                OOO00OO00OO000O0O =urllib .request .Request (O000O00000OOO00O0 ,headers =O0O000OO00O00OO0O )#line:2297
                O000OOO00O0OO00O0 =urllib .request .urlopen (OOO00OO00OO000O0O ,timeout =5 ).read ()#line:2298
            else :#line:2299
                OOO00OO00OO000O0O =urllib2 .Request (O000O00000OOO00O0 ,headers =O0O000OO00O00OO0O )#line:2300
                O000OOO00O0OO00O0 =urllib2 .urlopen (OOO00OO00OO000O0O ,timeout =5 ).read ()#line:2301
            O0000O0000OO0O00O .data =json .loads (O000OOO00O0OO00O0 )#line:2302
            if len (O0000O0000OO0O00O .data ["results"])==0 :#line:2303
                raise KeyError #line:2304
        except :#line:2305
            print ("503 Error")#line:2307
            O0000O0000OO0O00O .canvas .yview_moveto (0 )#line:2308
            for O0O000O000000OOOO in O0000O0000OO0O00O .canvas_frame .winfo_children ():#line:2309
                O0O000O000000OOOO .destroy ()#line:2310
            O0000O0000OO0O00O .search_button .config (state ="normal")#line:2311
            O0000O0000OO0O00O .parent .after_cancel (O0000O0000OO0O00O .search_after )#line:2312
            O0000O0000OO0O00O .is_searching =False #line:2313
            O0000O0000OO0O00O .search_gif .lower ()#line:2314
            O0000O0000OO0O00O .search_gif .config (image ="")#line:2315
            O0000O0000OO0O00O .current_page =current_page #line:2316
            O0000O0000OO0O00O .message_frame =tk .Label (O0000O0000OO0O00O .results_frame ,bg ="white",cursor ="hand2",justify =tk .CENTER ,anchor ='center')#line:2318
            O0000O0000OO0O00O .message_frame .grid_columnconfigure (0 ,weight =1 )#line:2319
            O0000O0000OO0O00O .message_frame .grid_rowconfigure (0 ,weight =1 )#line:2320
            O0000O0000OO0O00O .message_frame .grid (row =0 ,column =0 ,sticky ='NEWS')#line:2321
            O0000O0000OO0O00O .empty_result_text =tk .Text (O0000O0000OO0O00O .message_frame ,bg ="white",cursor ="hand2",relief =tk .FLAT )#line:2323
            O0000O0000OO0O00O .empty_result_text .grid (row =0 ,column =0 ,sticky ="EW")#line:2324
            O0000O0000OO0O00O .empty_result_text .tag_configure ('keyword_font',font =('Open Sans',11 ,"bold"))#line:2325
            O0000O0000OO0O00O .empty_result_text .tag_configure ('normal_font',font =('Open Sans',11 ))#line:2326
            O0000O0000OO0O00O .empty_result_text .tag_configure ('underline_font',font =('Open Sans',11 ,"underline"))#line:2327
            O0000O0000OO0O00O .empty_result_text .tag_configure ('justify_center',justify =tk .CENTER )#line:2328
            O0000O0000OO0O00O .empty_result_text .insert (tk .END ,"Your search for - ",('normal_font','justify_center'))#line:2329
            O0000O0000OO0O00O .empty_result_text .insert (tk .END ,O0000O0000OO0O00O .search_entry .get (),('keyword_font','justify_center'))#line:2330
            O0000O0000OO0O00O .empty_result_text .insert (tk .END ," - did not match any parts.\nBut, never fear! You can request it ",('normal_font','justify_center'))#line:2331
            O0000O0000OO0O00O .empty_result_text .insert (tk .END ,"here",('underline_font','justify_center'))#line:2332
            O0000O0000OO0O00O .empty_result_text .config (state =tk .DISABLED )#line:2333
            O0000O0000OO0O00O .empty_result_text .bind ('<Button-1>',O0000O0000OO0O00O .request_callback )#line:2337
            O0000O0000OO0O00O .search_button .config (state ="normal")#line:2340
            O0000O0000OO0O00O .parent .after_cancel (O0000O0000OO0O00O .search_after )#line:2341
            O0000O0000OO0O00O .search_entry .config (state ="normal")#line:2342
            return #line:2344
        O0000O0000OO0O00O .page_names =[]#line:2345
        if O0000O0000OO0O00O .max_page ==0 :#line:2346
            O0000O0000OO0O00O .max_page =1 #line:2347
            O0000O0000OO0O00O .page_names .append (1 )#line:2348
            O0000O0000OO0O00O .selected_index =0 #line:2349
        else :#line:2350
            for OOOOOOOO0O0O0O0O0 in O0000O0000OO0O00O .data ["pages"]:#line:2351
                O0000O0000OO0O00O .page_names .append (int (OOOOOOOO0O0O0O0O0 ["name"]))#line:2352
                if OOOOOOOO0O0O0O0O0 ["is_current"]:#line:2353
                    O0000O0000OO0O00O .selected_index =len (O0000O0000OO0O00O .page_names )-1 #line:2354
            if len (O0000O0000OO0O00O .page_names )>0 :#line:2355
                O0000O0000OO0O00O .max_page =max (O0000O0000OO0O00O .page_names )#line:2356
            else :#line:2357
                O0000O0000OO0O00O .max_page =0 #line:2358
        O0000O0000OO0O00O .canvas .yview_moveto (0 )#line:2361
        O0000O0000OO0O00O .canvas_frame .grid_rowconfigure (0 ,weight =0 )#line:2362
        for O000OOOOO0OOOO0OO in range (19 ):#line:2363
            O0000O0000OO0O00O .canvas_frame .grid_rowconfigure (O000OOOOO0OOOO0OO +1 ,weight =0 )#line:2364
        for O0O000O000000OOOO in O0000O0000OO0O00O .canvas_frame .winfo_children ():#line:2365
            O0O000O000000OOOO .destroy ()#line:2366
        for O000OOOOO0OOOO0OO in range (5 ):#line:2370
            O0000O0000OO0O00O .canvas_frame .grid_rowconfigure (O000OOOOO0OOOO0OO +1 ,weight =1 )#line:2371
        for O000OOOOO0OOOO0OO in range (len (O0000O0000OO0O00O .data ["results"])):#line:2372
            O0000O0000OO0O00O .canvas_frame .grid_rowconfigure (O000OOOOO0OOOO0OO +1 ,weight =1 )#line:2373
        O0000O0000OO0O00O .i =1 #line:2374
        O0000O0000OO0O00O .manufacturer_labels =[]#line:2375
        O0000O0000OO0O00O .available_labels =[]#line:2376
        O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (0 ,weight =2 )#line:2377
        O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (1 ,weight =2 )#line:2378
        O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (2 ,weight =2 )#line:2379
        O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (3 ,weight =2 )#line:2380
        O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (4 ,weight =2 )#line:2381
        O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (5 ,weight =1 )#line:2382
        O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (6 ,weight =3 )#line:2383
        O0000O0000OO0O00O .canvas_frame .update ()#line:2401
        O0O0OOO0O0O0OO00O ="#304E70"#line:2404
        if not O0000O0000OO0O00O .side_opened :#line:2406
            OOO000OOOO00OO0OO =tk .Frame (O0000O0000OO0O00O .canvas_frame ,bg ="#E1E1E1")#line:2407
            OOO000OOOO00OO0OO .grid_columnconfigure (0 ,weight =1 )#line:2408
            OOO000OOOO00OO0OO .grid_rowconfigure (0 ,weight =1 )#line:2409
            OOO000OOOO00OO0OO .grid (row =0 ,column =0 ,columnspan =1 ,sticky ="NEWS",padx =(5 ,0 ))#line:2417
            OO00O00O0O000O0O0 =tk .Label (OOO000OOOO00OO0OO ,fg =O0O0OOO0O0O0OO00O ,bg ="white",font =("Open Sans",9 ,"bold"),text ="Manufacturer")#line:2425
            OO00O00O0O000O0O0 .grid (row =0 ,column =0 ,columnspan =1 ,sticky ="NEWS",pady =(0 ,1 ))#line:2433
            O0000O0000OO0O00O .manufacturer_labels .append (OOO000OOOO00OO0OO )#line:2434
        O0O0OO00O00OOOOOO =tk .Frame (O0000O0000OO0O00O .canvas_frame ,bg ="#E1E1E1")#line:2436
        O0O0OO00O00OOOOOO .grid_columnconfigure (0 ,weight =1 )#line:2437
        O0O0OO00O00OOOOOO .grid_rowconfigure (0 ,weight =1 )#line:2438
        O0O0OO00O00OOOOOO .grid (row =0 ,column =1 ,columnspan =1 ,sticky ="NEWS",padx =(0 ,0 ))#line:2446
        tk .Label (O0O0OO00O00OOOOOO ,fg =O0O0OOO0O0O0OO00O ,bg ="white",height =4 ,font =("Open Sans",9 ,"bold"),text ="Image").grid (row =0 ,column =0 ,sticky ="NEWS",pady =(0 ,1 ))#line:2461
        OOO0OOO00OOOO0000 =tk .Frame (O0000O0000OO0O00O .canvas_frame ,bg ="#E1E1E1")#line:2462
        OOO0OOO00OOOO0000 .grid_columnconfigure (0 ,weight =1 )#line:2463
        OOO0OOO00OOOO0000 .grid_rowconfigure (0 ,weight =1 )#line:2464
        OOO0OOO00OOOO0000 .grid (row =0 ,column =2 ,columnspan =2 ,sticky ="NEWS")#line:2469
        tk .Label (OOO0OOO00OOOO0000 ,fg =O0O0OOO0O0O0OO00O ,bg ="white",font =("Open Sans",9 ,"bold"),text ="Part").grid (row =0 ,column =0 ,columnspan =1 ,pady =(0 ,1 ),sticky ="NEWS")#line:2483
        OOOOOO00OO00OO00O =tk .Frame (O0000O0000OO0O00O .canvas_frame ,bg ="#E1E1E1")#line:2508
        OOOOOO00OO00OO00O .grid_columnconfigure (0 ,weight =1 )#line:2509
        OOOOOO00OO00OO00O .grid_rowconfigure (0 ,weight =1 )#line:2510
        OOOOOO00OO00OO00O .grid (row =0 ,column =4 ,columnspan =1 ,padx =(0 ,0 ),sticky ="NEWS")#line:2516
        tk .Label (OOOOOO00OO00OO00O ,fg =O0O0OOO0O0O0OO00O ,bg ="white",anchor ="w",font =("Open Sans",9 ,"bold"),text ="       Description").grid (row =0 ,column =0 ,columnspan =1 ,pady =(0 ,1 ),sticky ="NEWS")#line:2530
        OO0OO0OO0000OOOO0 =tk .Frame (O0000O0000OO0O00O .canvas_frame ,bg ="#E1E1E1")#line:2531
        OO0OO0OO0000OOOO0 .grid_columnconfigure (0 ,weight =1 )#line:2532
        OO0OO0OO0000OOOO0 .grid_rowconfigure (0 ,weight =1 )#line:2533
        OO0OO0OO0000OOOO0 .grid (row =0 ,column =5 ,columnspan =1 ,sticky ="NEWS")#line:2538
        tk .Label (OO0OO0OO0000OOOO0 ,fg =O0O0OOO0O0O0OO00O ,bg ="white",font =("Open Sans",9 ,"bold"),text ="Package").grid (row =0 ,column =0 ,pady =(0 ,1 ),sticky ="NEWS")#line:2550
        O000OO0O00OO000O0 =tk .Frame (O0000O0000OO0O00O .canvas_frame ,bg ="#E1E1E1")#line:2551
        O000OO0O00OO000O0 .grid_columnconfigure (0 ,weight =1 )#line:2552
        O000OO0O00OO000O0 .grid_rowconfigure (0 ,weight =1 )#line:2553
        O000OO0O00OO000O0 .grid (row =0 ,column =6 ,columnspan =1 ,sticky ="NEWS")#line:2558
        tk .Label (O000OO0O00OO000O0 ,fg =O0O0OOO0O0O0OO00O ,bg ="white",font =("Open Sans",9 ,"bold"),text ="Data Available").grid (row =0 ,column =0 ,pady =(0 ,1 ),sticky ="NEWS")#line:2570
        O0000O0000OO0O00O .results_frame .update ()#line:2573
        O0000O0000OO0O00O .dual_frame .update ()#line:2574
        O00O00OO0O000O0OO =len (O0000O0000OO0O00O .data ["results"])*O0000O0000OO0O00O .results_frame .winfo_height ()/6 #line:2575
        O0000O0000OO0O00O .canvas .update ()#line:2576
        O0000O0000OO0O00O .canvas .itemconfigure ("inner_frame",height =400 )#line:2579
        O0000O0000OO0O00O .canvas_frame .config (height =400 )#line:2580
        if len (O0000O0000OO0O00O .data ["results"])>6 :#line:2581
            O0000O0000OO0O00O .canvas .itemconfigure ("inner_frame",height =O00O00OO0O000O0OO )#line:2582
            OO00O00O0OOO0O00O =ttk .Style ()#line:2583
            OO00O00O0OOO0O00O .theme_use ('clam')#line:2584
            OO00O00O0OOO0O00O .configure ("snapeda.Vertical.TScrollbar",gripcount =0 ,background ="#FF8330",troughcolor ='#C4C4C4',lightcolor ='#C4C4C4',darkcolor ='#C4C4C4',bordercolor ="#C4C4C4",borderwidth =0 ,relief =tk .FLAT )#line:2585
            OO00O00O0OOO0O00O .map ('snapeda.Vertical.TScrollbar',foreground =[('disabled','#C4C4C4'),('pressed','#FF8330'),('active','#FF8330')],background =[('disabled','#C4C4C4'),('pressed','!focus','#FF8330'),('active','#FF8330')],highlightcolor =[('focus','#C4C4C4'),('!focus','#C4C4C4')],)#line:2593
            OO00O00O0OOO0O00O .layout ('snapeda.Vertical.TScrollbar',[('Vertical.Scrollbar.trough',{'children':[('Vertical.Scrollbar.thumb',{'expand':'1','sticky':'nswe'})],'sticky':'ns'})])#line:2595
            O0000O0000OO0O00O .vsb =ttk .Scrollbar (O0000O0000OO0O00O .results_frame ,orient ="vertical",command =O0000O0000OO0O00O .canvas .yview ,style ="snapeda.Vertical.TScrollbar")#line:2596
            O0000O0000OO0O00O .canvas .bind_all ("<MouseWheel>",O0000O0000OO0O00O .mouse_wheel_callback )#line:2597
            O0000O0000OO0O00O .vsb .grid (row =0 ,column =1 ,sticky ='NS')#line:2598
            O0000O0000OO0O00O .canvas .config (yscrollcommand =O0000O0000OO0O00O .vsb .set )#line:2599
            O0000O0000OO0O00O .canvas .config (scrollregion =O0000O0000OO0O00O .canvas .bbox ("all"))#line:2600
        print ("frame height %d"%O0000O0000OO0O00O .results_frame .winfo_height ())#line:2602
        print ("height %d"%O00O00OO0O000O0OO )#line:2603
        print ("searched")#line:2605
        OOOOOO00OO0O0OO00 =15 #line:2607
        O0OOOOO0O0OO0000O =tk .PhotoImage (file =O0000O0000OO0O00O .datasheet_available_dir )#line:2608
        OOO00O000O00OO00O =O0000O0000OO0O00O .resize (O0OOOOO0O0OO0000O ,OOOOOO00OO0O0OO00 ,OOOOOO00OO0O0OO00 )#line:2609
        O0000O0000OO0O00O .parent .images .append (OOO00O000O00OO00O )#line:2610
        O0O00000OOOO00OO0 =tk .PhotoImage (file =O0000O0000OO0O00O .datasheet_not_available_dir )#line:2611
        O0O0OO0OO00OOOO00 =O0000O0000OO0O00O .resize (O0O00000OOOO00OO0 ,OOOOOO00OO0O0OO00 ,OOOOOO00OO0O0OO00 )#line:2612
        O0000O0000OO0O00O .parent .images .append (O0O0OO0OO00OOOO00 )#line:2613
        O00OO0O0O0O000OOO =tk .PhotoImage (file =O0000O0000OO0O00O .symbol_available_dir )#line:2615
        OOO0OOO00OOOOO0OO =O0000O0000OO0O00O .resize (O00OO0O0O0O000OOO ,OOOOOO00OO0O0OO00 ,OOOOOO00OO0O0OO00 )#line:2616
        O0000O0000OO0O00O .parent .images .append (OOO0OOO00OOOOO0OO )#line:2617
        O000OO0O0OO0OOO0O =tk .PhotoImage (file =O0000O0000OO0O00O .symbol_not_available_dir )#line:2618
        O00OOOO0000OOOO0O =O0000O0000OO0O00O .resize (O000OO0O0OO0OOO0O ,OOOOOO00OO0O0OO00 ,OOOOOO00OO0O0OO00 )#line:2619
        O0000O0000OO0O00O .parent .images .append (O00OOOO0000OOOO0O )#line:2620
        OOOO0O0O0OO0000O0 =tk .PhotoImage (file =O0000O0000OO0O00O .footprint_available_dir )#line:2622
        OOOO0000OOO0O000O =O0000O0000OO0O00O .resize (OOOO0O0O0OO0000O0 ,OOOOOO00OO0O0OO00 ,OOOOOO00OO0O0OO00 )#line:2623
        O0000O0000OO0O00O .parent .images .append (OOOO0000OOO0O000O )#line:2624
        O0OOOO0OO000OOOOO =tk .PhotoImage (file =O0000O0000OO0O00O .footprint_not_available_dir )#line:2625
        OO00O00O0OOOOOOOO =O0000O0000OO0O00O .resize (O0OOOO0OO000OOOOO ,OOOOOO00OO0O0OO00 ,OOOOOO00OO0O0OO00 )#line:2626
        O0000O0000OO0O00O .parent .images .append (OO00O00O0OOOOOOOO )#line:2627
        O000OOOO0OO00O00O =tk .PhotoImage (file =O0000O0000OO0O00O .threedee_available_dir )#line:2629
        OOOO0000000OOOO0O =O0000O0000OO0O00O .resize (O000OOOO0OO00O00O ,OOOOOO00OO0O0OO00 ,OOOOOO00OO0O0OO00 )#line:2630
        O0000O0000OO0O00O .parent .images .append (OOOO0000000OOOO0O )#line:2631
        OO00OOOOO0OO00O0O =tk .PhotoImage (file =O0000O0000OO0O00O .threedee_unavailable_dir )#line:2632
        O0O0OO0OO0O000OOO =O0000O0000OO0O00O .resize (OO00OOOOO0OO00O0O ,OOOOOO00OO0O0OO00 ,OOOOOO00OO0O0OO00 )#line:2633
        O0000O0000OO0O00O .parent .images .append (O0O0OO0OO0O000OOO )#line:2634
        O0000O0000OO0O00O .organization_images ={}#line:2636
        O0000O0000OO0O00O .manufacturer_names =[]#line:2637
        O0000O0000OO0O00O .is_searching =False #line:2639
        O0000O0000OO0O00O .search_gif .lower ()#line:2640
        O0000O0000OO0O00O .search_gif .config (image ="")#line:2641
        for O00OOO00OOO0OO0OO in O0000O0000OO0O00O .data ["results"]:#line:2643
            O00O000OO0O0OO0O0 =O0000O0000OO0O00O .i -1 #line:2645
            O0000O0000OO0O00O .intense_caverns_links .insert (O00O000OO0O0OO0O0 ,None )#line:2646
            O0000O0000OO0O00O .intense_caverns_img_dir .insert (O00O000OO0O0OO0O0 ,None )#line:2647
            O0000O0000OO0O00O .intense_caverns_thread_started .insert (O00O000OO0O0OO0O0 ,False )#line:2648
            O0O0000OO000OOOO0 =threading .Thread (target =O0000O0000OO0O00O .get_intense_caverns_link ,args =(O00O000OO0O0OO0O0 ,))#line:2649
            O0O0000OO000OOOO0 .setDaemon (True )#line:2650
            O0O0000OO000OOOO0 .start ()#line:2651
            if O0000O0000OO0O00O .i %2 ==0 :#line:2653
                OOO00O0OOO0O0O00O ="white"#line:2654
            else :#line:2655
                OOO00O0OOO0O0O00O ="white"#line:2657
            OO0O0OO00OO000O00 =""#line:2658
            if any ([O00OOO00OOO0OO0OO ["has_footprint"],O00OOO00OOO0OO0OO ["has_datasheet"],O00OOO00OOO0OO0OO ["has_symbol"]]):#line:2662
                if O00OOO00OOO0OO0OO ["has_footprint"]:#line:2663
                    OO0O0OO00OO000O00 +="Footprint, "#line:2664
                if O00OOO00OOO0OO0OO ["has_datasheet"]:#line:2665
                    OO0O0OO00OO000O00 +="Datasheet, "#line:2666
                if O00OOO00OOO0OO0OO ["has_symbol"]:#line:2667
                    OO0O0OO00OO000O00 +="Symbol"#line:2668
                if OO0O0OO00OO000O00 .endswith (", "):#line:2669
                    OO0O0OO00OO000O00 =OO0O0OO00OO000O00 [:-2 ]#line:2670
            else :#line:2671
                OO0O0OO00OO000O00 ="No Data"#line:2672
            O0000O0000OO0O00O .is_loading =False #line:2693
            if not O0000O0000OO0O00O .side_opened :#line:2695
                try :#line:2696
                    OOO0OO0OOOOOO0O00 =O00OOO00OOO0OO0OO ["organization_image_100_20"]#line:2697
                    OOO000OO00O0O00OO =O0000O0000OO0O00O .download_image (OOO0OO0OOOOOO0O00 )#line:2698
                    OOOOOO00OO0O0O0O0 =tk .PhotoImage (file =OOO000OO00O0O00OO )#line:2699
                    O00O00O0O000OO00O =O0000O0000OO0O00O .resize (OOOOOO00OO0O0O0O0 ,100 ,20 )#line:2700
                    O0000O0000OO0O00O .parent .images .append (O00O00O0O000OO00O )#line:2701
                    O0000O0000OO0O00O .organization_images [O0000O0000OO0O00O .i ]=O00O00O0O000OO00O #line:2702
                    O00OO0O0OOOOO00O0 =tk .Label (O0000O0000OO0O00O .canvas_frame ,image =O00O00O0O000OO00O ,bg =OOO00O0OOO0O0O00O ,font =("Open Sans",9 ),cursor ="hand2")#line:2703
                    O00OO0O0OOOOO00O0 .grid (row =O0000O0000OO0O00O .i ,column =0 ,columnspan =1 ,sticky ="NESW")#line:2704
                    O00OO0O0OOOOO00O0 .bind ("<Button-1>",lambda O000000OOOO0000O0 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O000000OOOO0000O0 ,index ))#line:2705
                except BaseException :#line:2706
                    print ("No Organization Image")#line:2707
                    O0000O0000OO0O00O .organization_image =None #line:2708
                    print (O00OOO00OOO0OO0OO )#line:2709
                    O00OO0O0OOOOO00O0 =tk .Label (O0000O0000OO0O00O .canvas_frame ,text =O00OOO00OOO0OO0OO ["manufacturer"],bg =OOO00O0OOO0O0O00O ,font =("Open Sans",9 ),cursor ="hand2")#line:2710
                    O00OO0O0OOOOO00O0 .grid (row =O0000O0000OO0O00O .i ,column =0 ,columnspan =1 ,sticky ="NESW")#line:2711
                    O00OO0O0OOOOO00O0 .bind ("<Button-1>",lambda OOOO0O00O0O0O0O00 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (OOOO0O00O0O0O0O00 ,index ))#line:2712
                O0000O0000OO0O00O .manufacturer_labels .append (O00OO0O0OOOOO00O0 )#line:2713
            try :#line:2715
                OOO00O0000O000O00 =O00OOO00OOO0OO0OO ["coverart"][0 ]["url"]#line:2716
                OOO000OO00O0O00OO =O0000O0000OO0O00O .download_image (OOO00O0000O000O00 )#line:2717
                OOOO0000O000O0000 =tk .PhotoImage (file =OOO000OO00O0O00OO )#line:2718
                OO000OOO00OOO00OO =O0000O0000OO0O00O .resize (OOOO0000O000O0000 ,55 ,55 )#line:2719
                O0000O0000OO0O00O .parent .images .append (OO000OOO00OOO00OO )#line:2720
                O0OO000000O00OO00 =tk .Label (O0000O0000OO0O00O .canvas_frame ,bg =OOO00O0OOO0O0O00O ,image =OO000OOO00OOO00OO ,cursor ="hand2")#line:2721
                O0OO000000O00OO00 .bind ("<Button-1>",lambda O0000O0OOOOO0O00O ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O0000O0OOOOO0O00O ,index ))#line:2722
                O0OO000000O00OO00 .grid (row =O0000O0000OO0O00O .i ,column =1 ,columnspan =1 ,sticky ="NESW")#line:2723
            except BaseException :#line:2724
                print ("No Symbol Image")#line:2725
                O0OO000000O00OO00 =tk .Label (O0000O0000OO0O00O .canvas_frame ,bg =OOO00O0OOO0O0O00O ,cursor ="hand2")#line:2726
                O0OO000000O00OO00 .grid (row =O0000O0000OO0O00O .i ,column =1 ,columnspan =1 ,sticky ="NESW")#line:2727
                O0OO000000O00OO00 .bind ("<Button-1>",lambda O00OOO0OOOO000O00 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O00OOO0OOOO000O00 ,index ))#line:2728
            OOO0OOO00OOOO0000 =tk .Frame (O0000O0000OO0O00O .canvas_frame ,bg =OOO00O0OOO0O0O00O ,cursor ="hand2")#line:2730
            OOO0OOO00OOOO0000 .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:2731
            OOO0OOO00OOOO0000 .grid_rowconfigure (1 ,weight =1 ,uniform ="foo")#line:2732
            OOO0OOO00OOOO0000 .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:2733
            OOO0OOO00OOOO0000 .grid (row =O0000O0000OO0O00O .i ,column =2 ,columnspan =2 ,sticky ="NEWS")#line:2734
            OOO0OOO00OOOO0000 .bind ("<Button-1>",lambda O0O000000O0O00OO0 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O0O000000O0O00OO0 ,index ))#line:2735
            OOO0O0O0OOO0OOO0O =tk .Label (OOO0OOO00OOOO0000 ,text =O00OOO00OOO0OO0OO ["part_number"],fg ="#304E70",bg =OOO00O0OOO0O0O00O ,font =("Open Sans",9 ),cursor ="hand2")#line:2744
            OOO0O0O0OOO0OOO0O .grid (row =0 ,column =0 ,columnspan =2 ,sticky ="S")#line:2749
            OOO0O0O0OOO0OOO0O .bind ("<Button-1>",lambda OOO00O0O0OOOO0OOO ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (OOO00O0O0OOOO0OOO ,index ))#line:2750
            O0O0OOO0O0O0OO0O0 =tk .Label (OOO0OOO00OOOO0000 ,text =O00OOO00OOO0OO0OO ["manufacturer"],bg =OOO00O0OOO0O0O00O ,font =("Open Sans",9 ),cursor ="hand2")#line:2758
            O0O0OOO0O0O0OO0O0 .grid (row =1 ,column =0 ,sticky ="N")#line:2762
            O0O0OOO0O0O0OO0O0 .bind ("<Button-1>",lambda O000OO0OO0OO0O0O0 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O000OO0OO0OO0O0O0 ,index ))#line:2763
            O0000O0000OO0O00O .manufacturer_names .append (O0O0OOO0O0O0OO0O0 )#line:2764
            OOOOOO00OO00OO00O =tk .Message (O0000O0000OO0O00O .canvas_frame ,bg =OOO00O0OOO0O0O00O ,cursor ="hand2")#line:2771
            OOOOOO00OO00OO00O .grid (row =O0000O0000OO0O00O .i ,column =4 ,columnspan =1 ,sticky ="NEWS")#line:2772
            OOOOOO00OO00OO00O .grid_columnconfigure (0 ,weight =1 )#line:2773
            OOOOOO00OO00OO00O .grid_rowconfigure (0 ,weight =1 )#line:2774
            OOOOOO00OO00OO00O .bind ("<Button-1>",lambda O0OO00O00O0O00O00 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O0OO00O00O0O00O00 ,index ))#line:2775
            OO00O0O0OOOO0OOOO =O00OOO00OOO0OO0OO ["short_description"]#line:2776
            if len (OO00O0O0OOOO0OOOO )>85 :#line:2777
                OO00O0O0OOOO0OOOO =OO00O0O0OOOO0OOOO [:50 ]+"..."#line:2778
            O000O000O0O0OO0OO =tk .Message (OOOOOO00OO00OO00O ,bg =OOO00O0OOO0O0O00O ,text =OO00O0O0OOOO0OOOO ,font =("Open Sans",8 ),cursor ="hand2",justify =tk .LEFT )#line:2781
            O000O000O0O0OO0OO .grid (row =0 ,column =0 ,sticky ="W",padx =(15 ,0 ))#line:2782
            O000O000O0O0OO0OO .bind ("<Button-1>",lambda OOOO0O00OOOO00000 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (OOOO0O00OOOO00000 ,index ))#line:2783
            if O00OOO00OOO0OO0OO ["package"]["name"]=="--------":#line:2784
                O00OOO00OOO0OO0OO ["package"]["name"]="N/A"#line:2785
            OOO0O000OOO00OOOO =tk .Label (O0000O0000OO0O00O .canvas_frame ,bg =OOO00O0OOO0O0O00O ,text =O00OOO00OOO0OO0OO ["package"]["name"],font =("Open Sans",9 ),cursor ="hand2")#line:2786
            OOO0O000OOO00OOOO .grid (row =O0000O0000OO0O00O .i ,column =5 ,columnspan =1 ,sticky ="NESW")#line:2787
            OOO0O000OOO00OOOO .bind ("<Button-1>",lambda O0O00OOO0O0OOOO0O ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O0O00OOO0O0OOOO0O ,index ))#line:2788
            OO00O00OO0O0000O0 =tk .Frame (O0000O0000OO0O00O .canvas_frame ,bg =OOO00O0OOO0O0O00O )#line:2790
            OO00O00OO0O0000O0 .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:2791
            OO00O00OO0O0000O0 .grid_columnconfigure (1 ,weight =1 ,uniform ="foo")#line:2792
            OO00O00OO0O0000O0 .grid_columnconfigure (2 ,weight =1 ,uniform ="foo")#line:2793
            OO00O00OO0O0000O0 .grid_columnconfigure (3 ,weight =1 ,uniform ="foo")#line:2794
            OO00O00OO0O0000O0 .grid_rowconfigure (0 ,weight =1 )#line:2795
            OO00O00OO0O0000O0 .grid (row =O0000O0000OO0O00O .i ,column =6 ,columnspan =1 ,sticky ="NESW")#line:2796
            OO00O00OO0O0000O0 .bind ("<Button-1>",lambda OO00000000OOOOOOO ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (OO00000000OOOOOOO ,index ))#line:2797
            if O00OOO00OOO0OO0OO ["has_datasheet"]:#line:2799
                OOO00000OOO00O00O =tk .Label (OO00O00OO0O0000O0 ,bg =OOO00O0OOO0O0O00O ,image =OOO00O000O00OO00O ,cursor ="hand2")#line:2800
                OOO00000OOO00O00O .grid (row =0 ,column =0 ,sticky ="EW")#line:2801
                OOO00000OOO00O00O .bind ("<Button-1>",lambda O0OOO00OO00OOO00O ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O0OOO00OO00OOO00O ,index ))#line:2802
            else :#line:2803
                OOO00000OOO00O00O =tk .Label (OO00O00OO0O0000O0 ,bg =OOO00O0OOO0O0O00O ,image =O0O0OO0OO00OOOO00 ,cursor ="hand2")#line:2804
                OOO00000OOO00O00O .grid (row =0 ,column =0 ,sticky ="EW")#line:2805
                OOO00000OOO00O00O .bind ("<Button-1>",lambda O0OOOO0000OO00OO0 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O0OOOO0000OO00OO0 ,index ))#line:2806
            if O00OOO00OOO0OO0OO ["has_symbol"]:#line:2807
                OOO0000OO0O00O000 =tk .Label (OO00O00OO0O0000O0 ,bg =OOO00O0OOO0O0O00O ,image =OOO0OOO00OOOOO0OO ,cursor ="hand2")#line:2808
                OOO0000OO0O00O000 .grid (row =0 ,column =1 ,sticky ="EW")#line:2809
                OOO0000OO0O00O000 .bind ("<Button-1>",lambda OO00O00O0O00O00O0 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (OO00O00O0O00O00O0 ,index ))#line:2810
            else :#line:2811
                OOO0000OO0O00O000 =tk .Label (OO00O00OO0O0000O0 ,bg =OOO00O0OOO0O0O00O ,image =O00OOOO0000OOOO0O ,cursor ="hand2")#line:2812
                OOO0000OO0O00O000 .grid (row =0 ,column =1 ,sticky ="EW")#line:2813
                OOO0000OO0O00O000 .bind ("<Button-1>",lambda OOOOOOO0O0O00OO0O ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (OOOOOOO0O0O00OO0O ,index ))#line:2814
            if O00OOO00OOO0OO0OO ["has_footprint"]:#line:2815
                O0O0OOO0O0OOO00OO =tk .Label (OO00O00OO0O0000O0 ,bg =OOO00O0OOO0O0O00O ,image =OOOO0000OOO0O000O ,cursor ="hand2")#line:2816
                O0O0OOO0O0OOO00OO .grid (row =0 ,column =2 ,sticky ="EW")#line:2817
                O0O0OOO0O0OOO00OO .bind ("<Button-1>",lambda OO0O00O00O00OOO0O ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (OO0O00O00O00OOO0O ,index ))#line:2818
            else :#line:2819
                O0O0OOO0O0OOO00OO =tk .Label (OO00O00OO0O0000O0 ,bg =OOO00O0OOO0O0O00O ,image =OO00O00O0OOOOOOOO ,cursor ="hand2")#line:2820
                O0O0OOO0O0OOO00OO .grid (row =0 ,column =2 ,sticky ="EW")#line:2821
                O0O0OOO0O0OOO00OO .bind ("<Button-1>",lambda OOO0O000O0O00O0O0 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (OOO0O000O0O00O0O0 ,index ))#line:2822
            OOOO0000O000O00OO ='models'in O00OOO00OOO0OO0OO and len (O00OOO00OOO0OO0OO ["models"])>0 and '3dmodel_medium'in O00OOO00OOO0OO0OO ["models"][0 ]and 'url'in O00OOO00OOO0OO0OO ["models"][0 ]['3dmodel_medium']#line:2824
            if OOOO0000O000O00OO :#line:2825
                O0OO00OO00OO00000 =tk .Label (OO00O00OO0O0000O0 ,bg =OOO00O0OOO0O0O00O ,image =OOOO0000000OOOO0O ,cursor ="hand2")#line:2826
                O0OO00OO00OO00000 .grid (row =0 ,column =3 ,sticky ="EW")#line:2827
                O0OO00OO00OO00000 .bind ("<Button-1>",lambda O0000OO0O00OOOOO0 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O0000OO0O00OOOOO0 ,index ))#line:2828
            else :#line:2829
                O0OO00OO00OO00000 =tk .Label (OO00O00OO0O0000O0 ,bg =OOO00O0OOO0O0O00O ,image =O0O0OO0OO0O000OOO ,cursor ="hand2")#line:2830
                O0OO00OO00OO00000 .grid (row =0 ,column =3 ,sticky ="EW")#line:2831
                O0OO00OO00OO00000 .bind ("<Button-1>",lambda O0OO0OO0O000OOOO0 ,index =O0000O0000OO0O00O .i -1 :O0000O0000OO0O00O .on_tree_select (O0OO0OO0O000OOOO0 ,index ))#line:2832
            O0000O0000OO0O00O .i =O0000O0000OO0O00O .i +1 #line:2835
        O0OOOO0O000OO00O0 =tk .PhotoImage (file =O0000O0000OO0O00O .prev_bg_dir )#line:2837
        O00OOO00000O0OO0O =O0000O0000OO0O00O .resize (O0OOOO0O000OO00O0 ,55 ,55 )#line:2838
        O0000O0000OO0O00O .parent .images .append (O00OOO00000O0OO0O )#line:2839
        OO0OOO000000O0O00 =tk .PhotoImage (file =O0000O0000OO0O00O .next_bg_dir )#line:2840
        O000OOO00O0O000O0 =O0000O0000OO0O00O .resize (OO0OOO000000O0O00 ,55 ,55 )#line:2841
        O0000O0000OO0O00O .parent .images .append (O000OOO00O0O000O0 )#line:2842
        O0000O0000OO0O00O .pages_frame =tk .Frame (O0000O0000OO0O00O .table_frame ,bg ="#E1E1E1")#line:2843
        O0000O0000OO0O00O .pages_frame .grid (row =6 ,column =0 ,sticky ="W",padx =(0 ,0 ))#line:2844
        O0000O0000OO0O00O .pages_frame .grid_rowconfigure (0 ,weight =1 )#line:2845
        O0OOOOOOOO0O00000 =tk .PhotoImage (file =O0000O0000OO0O00O .selected_page_dir )#line:2846
        OO0000OOOOOO000OO =O0000O0000OO0O00O .resize (O0OOOOOOOO0O00000 ,25 ,25 )#line:2847
        O0000O0000OO0O00O .parent .images .append (OO0000OOOOOO000OO )#line:2848
        O0000O0000OO0O00O .pages =[]#line:2849
        for O000OOOOO0OOOO0OO in range (len (O0000O0000OO0O00O .page_names )):#line:2852
            O0000O0000OO0O00O .pages .append (tk .Label (O0000O0000OO0O00O .pages_frame ,bg ="white",text =str (O0000O0000OO0O00O .page_names [O000OOOOO0OOOO0OO ]),fg ="#304E70",cursor ="hand2",font =("Open Sans","10","bold"),width =4 ,height =2 ))#line:2867
            O0000O0000OO0O00O .pages [O000OOOOO0OOOO0OO ].grid (row =0 ,column =O000OOOOO0OOOO0OO +1 ,sticky ="NEWS",pady =(1 ,1 ))#line:2868
            O0000O0000OO0O00O .pages [O000OOOOO0OOOO0OO ].bind ("<Button-1>",lambda O0OOOO0000OOO000O ,current_page =O0000O0000OO0O00O .page_names [O000OOOOO0OOOO0OO ]:O0000O0000OO0O00O .search_data (O0OOOO0000OOO000O ,current_page =current_page ))#line:2869
        if O0000O0000OO0O00O .side_opened :#line:2871
            for OOOOO00O0OOOOOO0O in O0000O0000OO0O00O .manufacturer_names :#line:2872
                OOOOO00O0OOOOOO0O .config (fg ="#999999")#line:2873
            for O00OOOO0OOOO0OO00 in O0000O0000OO0O00O .manufacturer_labels :#line:2874
                O00OOOO0OOOO0OO00 .grid_forget ()#line:2875
            for O00OOOO0OOOO0OO00 in O0000O0000OO0O00O .available_labels :#line:2876
                O00OOOO0OOOO0OO00 .grid_forget ()#line:2877
            O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (0 ,weight =0 )#line:2878
            O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (1 ,weight =2 )#line:2879
            O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (2 ,weight =2 )#line:2880
            O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (3 ,weight =0 )#line:2881
            O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (4 ,weight =2 )#line:2882
            O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (5 ,weight =1 )#line:2883
            O0000O0000OO0O00O .canvas_frame .grid_columnconfigure (6 ,weight =3 )#line:2884
        O0000O0000OO0O00O .pages [O0000O0000OO0O00O .selected_index ].config (bg ="#FF761B",fg ="white")#line:2886
        O0000O0000OO0O00O .prev_button =tk .Label (O0000O0000OO0O00O .pages_frame ,text ="   < Prev   ",fg ="#FF761B",bg ="white",cursor ="hand2",font =("Open Sans","11","bold"))#line:2887
        O0000O0000OO0O00O .prev_button .grid (row =0 ,column =0 ,sticky ="NEWS",padx =(1 ,0 ),pady =(1 ,1 ))#line:2888
        O0000O0000OO0O00O .prev_button .bind ("<Button-1>",O0000O0000OO0O00O .prev_page )#line:2889
        O0000O0000OO0O00O .next_button =tk .Label (O0000O0000OO0O00O .pages_frame ,text ="   Next >   ",fg ="#FF761B",bg ="white",cursor ="hand2",font =("Open Sans","11","bold"))#line:2890
        O0000O0000OO0O00O .next_button .grid (row =0 ,column =len (O0000O0000OO0O00O .page_names )+1 ,sticky ="NEWS",padx =(0 ,1 ),pady =(1 ,1 ))#line:2891
        O0000O0000OO0O00O .next_button .bind ("<Button-1>",O0000O0000OO0O00O .next_page )#line:2892
        O0000O0000OO0O00O .search_button .config (state ="normal")#line:2895
        O0000O0000OO0O00O .parent .after_cancel (O0000O0000OO0O00O .search_after )#line:2896
        O0000O0000OO0O00O .search_entry .config (state ="normal")#line:2897
class WelcomeScreen (tk .Frame ):#line:2906
    ""#line:2909
    def __init__ (OOO00OOO0OO0OOOO0 ,O000O000O000O0OO0 ):#line:2911
        tk .Frame .__init__ (OOO00OOO0OO0OOOO0 ,O000O000O000O0OO0 )#line:2912
        OOO00OOO0OO0OOOO0 .parent =O000O000O000O0OO0 #line:2913
        OOO00OOO0OO0OOOO0 .dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:2914
        OOO00OOO0OO0OOOO0 .is_mac =platform .mac_ver ()[0 ]!=""#line:2915
        OOO00OOO0OO0OOOO0 .is_windows =(os .name =='nt')#line:2916
        if OOO00OOO0OO0OOOO0 .is_windows :#line:2917
            OOO00OOO0OO0OOOO0 .windata_dir =os .path .join (os .getenv ('HOMEDRIVE'),os .getenv ('HOMEPATH'),"SnapEDA Kicad Plugin")#line:2920
            OOO00OOO0OO0OOOO0 .flip_table_dir =os .path .join (os .getenv ('APPDATA'),'kicad','fp-lib-table')#line:2923
            OOO00OOO0OO0OOOO0 .appdata_dir =os .path .join (OOO00OOO0OO0OOOO0 .windata_dir ,"App")#line:2924
            if not os .path .exists (OOO00OOO0OO0OOOO0 .windata_dir ):#line:2925
                os .makedirs (OOO00OOO0OO0OOOO0 .windata_dir )#line:2926
            if not os .path .exists (OOO00OOO0OO0OOOO0 .appdata_dir ):#line:2927
                os .makedirs (OOO00OOO0OO0OOOO0 .appdata_dir )#line:2928
            OOO00OOO0OO0OOOO0 .kicad_library_dir =os .path .join (OOO00OOO0OO0OOOO0 .windata_dir ,'KiCad Library')#line:2929
            OO0O0OO0000O0O0O0 =os .path .join (OOO00OOO0OO0OOOO0 .kicad_library_dir ,'SnapEDA Library.pretty')#line:2931
            if not os .path .exists (OOO00OOO0OO0OOOO0 .kicad_library_dir ):#line:2932
                os .makedirs (OOO00OOO0OO0OOOO0 .kicad_library_dir )#line:2933
            if not os .path .exists (OO0O0OO0000O0O0O0 ):#line:2934
                os .makedirs (OO0O0OO0000O0O0O0 )#line:2935
        elif OOO00OOO0OO0OOOO0 .is_mac :#line:2936
            OOO00OOO0OO0OOOO0 .macdata_dir =os .path .join (os .path .expanduser ("~"),"Documents","SnapEDA Kicad Plugin")#line:2937
            OOO00OOO0OO0OOOO0 .appdata_dir =os .path .join (OOO00OOO0OO0OOOO0 .macdata_dir ,"App")#line:2938
            if not os .path .exists (OOO00OOO0OO0OOOO0 .appdata_dir ):#line:2939
                os .makedirs (OOO00OOO0OO0OOOO0 .appdata_dir )#line:2940
        else :#line:2941
            OOO00OOO0OO0OOOO0 .appdata_dir =os .path .join (OOO00OOO0OO0OOOO0 .dir_path ,"assets")#line:2942
            if not os .path .exists (OOO00OOO0OO0OOOO0 .appdata_dir ):#line:2943
                os .makedirs (OOO00OOO0OO0OOOO0 .appdata_dir )#line:2944
            OOO00OOO0OO0OOOO0 .flip_table_dir =os .path .join (os .path .expanduser ("~"),'.config','kicad','fp-lib-table')#line:2948
            OOOOOOO0O00OO0OO0 =os .path .expanduser ("~")#line:2949
            OOO00OOO0OO0OOOO0 .kicad_library_dir =os .path .join (OOOOOOO0O00OO0OO0 ,'KiCad Library')#line:2950
            OO0O0OO0000O0O0O0 =os .path .join (OOO00OOO0OO0OOOO0 .kicad_library_dir ,'SnapEDA Library.pretty')#line:2952
            if not os .path .exists (OOO00OOO0OO0OOOO0 .kicad_library_dir ):#line:2953
                os .makedirs (OOO00OOO0OO0OOOO0 .kicad_library_dir )#line:2954
            if not os .path .exists (OO0O0OO0000O0O0O0 ):#line:2955
                os .makedirs (OO0O0OO0000O0O0O0 )#line:2956
        OOO00OOO0OO0OOOO0 .icon_bitmap_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,"32x32.ico")#line:2958
        OOO00OOO0OO0OOOO0 .welcome_screen_001_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,"Mask+Group.png")#line:2959
        OOO00OOO0OO0OOOO0 .welcome_screen_002_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,"icon1.bbe45f7648f7.png")#line:2960
        OOO00OOO0OO0OOOO0 .welcome_screen_003_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,"ico_deadlines.8ba69c3f942a.png")#line:2961
        OOO00OOO0OO0OOOO0 .welcome_screen_004_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,"icon2.924b03ebfccc.png")#line:2962
        OOO00OOO0OO0OOOO0 .welcome_screen_005_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,"powered+by+snapEDA.png")#line:2963
        OOO00OOO0OO0OOOO0 .welcome_screen_006_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,"snapeda-transparent.png")#line:2964
        OOO00OOO0OO0OOOO0 .usb_type_c_button_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,"usb+type+c.png")#line:2965
        OOO00OOO0OO0OOOO0 .microcontroller_button_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,"usb+microcontroller.png")#line:2966
        OOO00OOO0OO0OOOO0 .how_it_works_menu_img_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,'how_it_works_menu.png')#line:2967
        OOO00OOO0OO0OOOO0 .info_menu_img_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,'info_menu.png')#line:2968
        OOO00OOO0OO0OOOO0 .settings_menu_img_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,'settings_menu.png')#line:2969
        if IS_UPDATED :#line:2971
            OOO00OOO0OO0OOOO0 .update_menu_img_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,'update_menu.png')#line:2972
        else :#line:2973
            OOO00OOO0OO0OOOO0 .update_menu_img_dir =os .path .join (OOO00OOO0OO0OOOO0 .appdata_dir ,'notif_update_menu+(2).png')#line:2974
        OOO00OOO0OO0OOOO0 .initialize_user_interface ()#line:2976
    def resize (OO0OO0O00O0000O00 ,O00000O0OO00O0000 ,OOO0O0O00O0O0OOOO ,OO00000O00OOOO0O0 ):#line:2978
        ""#line:2982
        if sys .version_info [0 ]==3 :#line:2983
            O000OOO0OO0000OOO =O00000O0OO00O0000 .width ()#line:2984
            OOOOOO0O0O0OO00O0 =O00000O0OO00O0000 .height ()#line:2985
            OO0OO0OO0O0O0OOOO =max (O000OOO0OO0000OOO ,OOOOOO0O0O0OO00O0 )#line:2986
            OOOO0000O0O000000 =max (OOO0O0O00O0O0OOOO ,OO00000O00OOOO0O0 )#line:2987
            if OO0OO0OO0O0O0OOOO >OOOO0000O0O000000 :#line:2988
                return O00000O0OO00O0000 .subsample (int (OO0OO0OO0O0O0OOOO /OOOO0000O0O000000 ))#line:2989
            else :#line:2990
                return O00000O0OO00O0000 .zoom (int (OOOO0000O0O000000 /OO0OO0OO0O0O0OOOO ))#line:2991
        else :#line:2992
            O000OOO0OO0000OOO =O00000O0OO00O0000 .width ()#line:2993
            OOOOOO0O0O0OO00O0 =O00000O0OO00O0000 .height ()#line:2994
            OO0OO0OO0O0O0OOOO =max (O000OOO0OO0000OOO ,OOOOOO0O0O0OO00O0 )#line:2995
            OOOO0000O0O000000 =max (OOO0O0O00O0O0OOOO ,OO00000O00OOOO0O0 )#line:2996
            if OO0OO0OO0O0O0OOOO >OOOO0000O0O000000 :#line:2997
                return O00000O0OO00O0000 .subsample (OO0OO0OO0O0O0OOOO /OOOO0000O0O000000 )#line:2998
            else :#line:2999
                return O00000O0OO00O0000 .zoom (OOOO0000O0O000000 /OO0OO0OO0O0O0OOOO )#line:3000
    def welcome_screen_search_callback (OO000OO00OO000000 ,O0OO0OOOOO0O000O0 ):#line:3002
        OO0O00OO00OOO0OOO =OO000OO00OO000000 .search_bar .get ()#line:3003
        if len (OO0O00OO00OOO0OOO )>0 :#line:3004
            for OOO0000OO000OOOO0 in range (5 ):#line:3005
                for O000O0OO0000OOOOO in OO000OO00OO000000 .parent .grid_slaves (row =OOO0000OO000OOOO0 ,column =0 ):#line:3006
                    O000O0OO0000OOOOO .destroy ()#line:3007
            OO000OO00OO000000 .parent .search_datum =OO0O00OO00OOO0OOO #line:3008
            OO000OO00OO000000 .search_bar .destroy ()#line:3010
            TableView (OO000OO00OO000000 .parent )#line:3011
    def usb_type_c_button_callback (OOOOOO000000O0O00 ,OO00OO0O0O0OOOO0O ):#line:3013
        for OO0O0O0O0O0O0OO0O in range (5 ):#line:3014
            for OO000OOOO00O0OOO0 in OOOOOO000000O0O00 .parent .grid_slaves (row =OO0O0O0O0O0O0OO0O ,column =0 ):#line:3015
                OO000OOOO00O0OOO0 .destroy ()#line:3016
        OOOOOO000000O0O00 .parent .search_datum ="usb type c"#line:3017
        TableView (OOOOOO000000O0O00 .parent )#line:3018
    def microcontroller_button_callback (OO00O00OO0O000OOO ,OO0OO000O0OOO0O00 ):#line:3020
        for OOO0OOOOOO0OOOOO0 in range (5 ):#line:3021
            for O000OOOO00OO0O000 in OO00O00OO0O000OOO .parent .grid_slaves (row =OOO0OOOOOO0OOOOO0 ,column =0 ):#line:3022
                O000OOOO00OO0O000 .destroy ()#line:3023
        OO00O00OO0O000OOO .parent .search_datum ="microcontroller"#line:3024
        TableView (OO00O00OO0O000OOO .parent )#line:3025
    def how_it_works_callback (OOO0O0O00000OOOO0 ,O0O000O000OO0OO0O ):#line:3027
        global IS_SETTING_WINDOW_OPEN #line:3028
        if IS_SETTING_WINDOW_OPEN is False :#line:3029
            OOO0O0O00000OOOO0 .parent .is_help_me_window =False #line:3030
            InfoView (OOO0O0O00000OOOO0 .parent )#line:3031
    def update_process (OOO0OOO0O0O00OO0O ):#line:3043
        OOO0OOO0O0O00OO0O .status_text .set ("Downloading update...")#line:3045
        OO00OO000000OOO0O =os .path .join (OOO0OOO0O0O00OO0O .kicad_library_dir ,'temp')#line:3046
        if not os .path .exists (OO00OO000000OOO0O ):#line:3047
                os .makedirs (OO00OO000000OOO0O )#line:3048
        if sys .version_info [0 ]==3 :#line:3049
            with urllib .request .urlopen ('https://snapeda.s3.amazonaws.com/plugins/kicad/SnapEDA-KiCad-Plugin.zip')as O0000000O0O0OOO00 ,open (os .path .join (OO00OO000000OOO0O ,'SnapEDA-KiCad-Plugin.zip'),'wb')as OOOO0O0O0000OOOO0 :#line:3050
                shutil .copyfileobj (O0000000O0O0OOO00 ,OOOO0O0O0000OOOO0 )#line:3051
        else :#line:3052
            O0000O000OOO0OOOO =urllib2 .urlopen ('https://snapeda.s3.amazonaws.com/plugins/kicad/SnapEDA-KiCad-Plugin.zip')#line:3053
            with open (os .path .join (OO00OO000000OOO0O ,'SnapEDA-KiCad-Plugin.zip'),"wb")as OOOO00O0O0O00OO00 :#line:3054
                shutil .copyfileobj (O0000O000OOO0OOOO ,OOOO00O0O0O00OO00 )#line:3055
        OOO0OOO0O0O00OO0O .status_text .set ("Extracting package...")#line:3057
        with zipfile .ZipFile (os .path .join (OO00OO000000OOO0O ,'SnapEDA-KiCad-Plugin.zip'))as O0OO0O0O00OO0O00O :#line:3059
            O0OO0O0O00OO0O00O .extractall (OO00OO000000OOO0O )#line:3060
        OOO0OOO0O0O00OO0O .status_text .set ("Copying files...")#line:3062
        for OO0000OOO000O000O in os .listdir (OO00OO000000OOO0O ):#line:3064
            if OO0000OOO000O000O .endswith (".py"):#line:3065
                copyfile (os .path .join (OO00OO000000OOO0O ,OO0000OOO000O000O ),os .path .join (os .path .dirname (os .path .realpath (__file__ )),OO0000OOO000O000O ))#line:3066
        shutil .rmtree (OO00OO000000OOO0O )#line:3068
        OOO0OOO0O0O00OO0O .status_text .set ("Update complete.")#line:3070
        OOO0OOO0O0O00OO0O .header_text .set ("UPDATE COMPLETE")#line:3072
        OOO0OOO0O0O00OO0O .subheader_text .set ("Update successful. Please restart SnapEDA, refresh the plugins, then open SnapEDA.")#line:3073
        OOO0OOO0O0O00OO0O .status_text .set ("")#line:3074
    def setting_callback (O0O00OOOO0OOO00OO ,OO000000000O0O000 ):#line:3076
        global IS_SETTING_WINDOW_OPEN #line:3077
        if IS_SETTING_WINDOW_OPEN is False :#line:3078
            SettingsView (O0O00OOOO0OOO00OO .parent )#line:3079
    def update_callback (OOOOO00OOO0OO0OO0 ,O00OO0O0OOO0OO00O ):#line:3081
        try :#line:3083
            OOOOOO0O0O0O00O00 =os .getuid ()==0 #line:3084
        except AttributeError :#line:3085
            OOOOOO0O0O0O00O00 =ctypes .windll .shell32 .IsUserAnAdmin ()!=0 #line:3086
        if not OOOOOO0O0O0O00O00 :#line:3088
            if OOOOO00OOO0OO0OO0 .is_windows :#line:3089
                tkMessageBox .showwarning ("Update","Please restart KiCAD as administrator, then update again.")#line:3090
                return #line:3091
        OOOOO00OOO0OO0OO0 .update_container =tk .Frame (OOOOO00OOO0OO0OO0 .parent ,bg ="#ff761a")#line:3096
        OOOOO00OOO0OO0OO0 .update_container .grid (row =0 ,column =0 ,sticky ="NEWS")#line:3097
        OOOOO00OOO0OO0OO0 .update_container .grid_columnconfigure (0 ,weight =1 )#line:3098
        for OOO000OO0O000O000 in range (4 ):#line:3099
            OOOOO00OOO0OO0OO0 .update_container .grid_rowconfigure (OOO000OO0O000O000 ,weight =1 ,uniform ="foo")#line:3100
        OOOOO00OOO0OO0OO0 .header_container =tk .Frame (OOOOO00OOO0OO0OO0 .update_container ,bg ="#ff761a")#line:3102
        OOOOO00OOO0OO0OO0 .header_container .grid (row =1 ,column =0 ,columnspan =1 ,sticky ="NEWS")#line:3103
        OOOOO00OOO0OO0OO0 .header_container .grid_columnconfigure (0 ,weight =1 )#line:3104
        for OOO000OO0O000O000 in range (3 ):#line:3105
            OOOOO00OOO0OO0OO0 .header_container .grid_rowconfigure (OOO000OO0O000O000 ,weight =1 ,uniform ="foo")#line:3106
        OOOOO00OOO0OO0OO0 .header_text =tk .StringVar ()#line:3108
        OOOOO00OOO0OO0OO0 .header_text .set ("UPDATING...")#line:3109
        OOOOO00OOO0OO0OO0 .header_label =tk .Label (OOOOO00OOO0OO0OO0 .header_container ,bg ="#ff761a",fg ="white",textvariable =OOOOO00OOO0OO0OO0 .header_text ,justify =tk .CENTER ,font =("Open Sans","18","bold"))#line:3110
        OOOOO00OOO0OO0OO0 .header_label .grid (row =0 ,column =0 ,columnspan =1 ,sticky ="NEWS")#line:3111
        OOOOO00OOO0OO0OO0 .subheader_text =tk .StringVar ()#line:3113
        OOOOO00OOO0OO0OO0 .subheader_text .set ("This may take a while, about 3-5 minutes. Mind to have a coffee break?")#line:3114
        OOOOO00OOO0OO0OO0 .subheader_label =tk .Label (OOOOO00OOO0OO0OO0 .header_container ,textvariable =OOOOO00OOO0OO0OO0 .subheader_text ,fg ="white",bg ="#ff761a",font =("Open Sans","13"))#line:3115
        OOOOO00OOO0OO0OO0 .subheader_label .grid (row =1 ,column =0 ,sticky ="NEW")#line:3116
        OOOOO00OOO0OO0OO0 .status_text =tk .StringVar ()#line:3118
        OOOOO00OOO0OO0OO0 .status_text .set ("Starting update...")#line:3119
        OOOOO00OOO0OO0OO0 .status_label =tk .Label (OOOOO00OOO0OO0OO0 .header_container ,textvariable =OOOOO00OOO0OO0OO0 .status_text ,fg ="white",bg ="#ff761a",font =("Open Sans","13","italic"))#line:3120
        OOOOO00OOO0OO0OO0 .status_label .grid (row =2 ,column =0 ,sticky ="NEW")#line:3121
        OOOOO00OOO0OO0OO0 .update_thread =threading .Thread (target =OOOOO00OOO0OO0OO0 .update_process )#line:3123
        OOOOO00OOO0OO0OO0 .update_thread .setDaemon (True )#line:3124
        OOOOO00OOO0OO0OO0 .update_thread .start ()#line:3125
    def help_me_callback (O0OO000OOOO0000OO ,O00O0O00O0OO0O000 ):#line:3128
        global IS_SETTING_WINDOW_OPEN #line:3129
        if IS_SETTING_WINDOW_OPEN is False :#line:3130
            O0OO000OOOO0000OO .parent .is_help_me_window =True #line:3131
            InfoView (O0OO000OOOO0000OO .parent )#line:3132
    def select_all_option (OOOO00O0O0OO00O0O ):#line:3136
        OOOO00O0O0OO00O0O .search_bar .focus ()#line:3137
        OOOO00O0O0OO00O0O .search_bar .index (tk .INSERT )#line:3138
        OO00OOO000O0O00OO =OOOO00O0O0OO00O0O .search_bar .selection_range (0 ,tk .END )#line:3139
    def cut_option (O00OO0OO0O0O00OO0 ):#line:3141
        if O00OO0OO0O0O00OO0 .search_bar .selection_present ():#line:3142
            O000OO0O000O0O0O0 =O00OO0OO0O0O00OO0 .search_bar .selection_get ()#line:3143
            O00OO0OO0O0O00OO0 .search_bar .delete ("sel.first","sel.last")#line:3144
            O00OO0OO0O0O00OO0 .parent .clipboard_clear ()#line:3146
            O00OO0OO0O0O00OO0 .parent .clipboard_append (O000OO0O000O0O0O0 )#line:3147
    def copy_option (O00O00OOO00OOOOOO ):#line:3149
        if O00O00OOO00OOOOOO .search_bar .selection_present ():#line:3150
            OO0OOOO0OOO0O00OO =O00O00OOO00OOOOOO .search_bar .selection_get ()#line:3151
            O00O00OOO00OOOOOO .parent .clipboard_clear ()#line:3153
            O00O00OOO00OOOOOO .parent .clipboard_append (OO0OOOO0OOO0O00OO )#line:3154
    def paste_option (OO0000O0O00OOO000 ):#line:3156
        O00O0000000OO0O00 =OO0000O0O00OOO000 .parent .clipboard_get ()#line:3157
        if OO0000O0O00OOO000 .search_bar .selection_present ():#line:3158
            OO0000O0O00OOO000 .search_bar .delete ("sel.first","sel.last")#line:3159
        OO0000O0O00OOO000 .search_bar .insert ('insert',O00O0000000OO0O00 )#line:3160
    def show_copy_paste_option (OOO0OO0O00000O00O ,O0OO0OOOOOO00O0OO ):#line:3162
        O0O000OOOO0OOOO00 =tk .Menu (OOO0OO0O00000O00O .parent ,tearoff =0 )#line:3163
        O0O000OOOO0OOOO00 .add_command (label ="Select All",command =OOO0OO0O00000O00O .select_all_option )#line:3164
        O0O000OOOO0OOOO00 .add_command (label ="Cut",command =OOO0OO0O00000O00O .cut_option )#line:3165
        O0O000OOOO0OOOO00 .add_command (label ="Copy",command =OOO0OO0O00000O00O .copy_option )#line:3166
        O0O000OOOO0OOOO00 .add_command (label ="Paste",command =OOO0OO0O00000O00O .paste_option )#line:3167
        try :#line:3171
            O0O000OOOO0OOOO00 .tk_popup (O0OO0OOOOOO00O0OO .x_root ,O0OO0OOOOOO00O0OO .y_root )#line:3172
        finally :#line:3173
            O0O000OOOO0OOOO00 .grab_release ()#line:3174
    def initialize_user_interface (O0OOO0O0O000O0OOO ):#line:3176
        if O0OOO0O0O000O0OOO .is_windows :#line:3177
            O0OOO0O0O000O0OOO .parent .iconbitmap (O0OOO0O0O000O0OOO .icon_bitmap_dir )#line:3178
        O0OOO0O0O000O0OOO .parent .title ("SnapEDA v"+O0OOO0O0O000O0OOO .parent .version )#line:3179
        O0OOO0O0O000O0OOO .parent .geometry ("1150x828")#line:3180
        O0OOO0O0O000O0OOO .parent .minsize (width =1150 ,height =828 )#line:3181
        O0OOO0O0O000O0OOO .parent .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:3182
        O0OOO0O0O000O0OOO .parent .grid_rowconfigure (0 ,weight =1 ,uniform ="foo")#line:3183
        O0OOO0O0O000O0OOO .parent_container =tk .Frame (O0OOO0O0O000O0OOO .parent ,bg ="white")#line:3184
        O0OOO0O0O000O0OOO .parent_container .grid (row =0 ,column =0 ,sticky ="NEWS")#line:3185
        O0OOO0O0O000O0OOO .parent_container .grid_columnconfigure (0 ,weight =1 ,uniform ="foo")#line:3186
        O0OOO0O0O000O0OOO .parent_container .grid_rowconfigure (0 ,weight =1 )#line:3187
        O0OOO0O0O000O0OOO .main_frame =tk .Frame (O0OOO0O0O000O0OOO .parent_container ,bg ="white")#line:3188
        O0OOO0O0O000O0OOO .main_frame .grid (row =0 ,column =0 ,columnspan =1 ,sticky ="NEWS")#line:3189
        for O0O000O0O0O00OO0O in range (3 ):#line:3190
            O0OOO0O0O000O0OOO .main_frame .grid_columnconfigure (O0O000O0O0O00OO0O ,weight =1 ,uniform ="foo")#line:3191
        O0OOO0O0O000O0OOO .main_frame .grid_rowconfigure (0 ,weight =1 )#line:3192
        O0OOO0O0O000O0OOO .left_frame =tk .Frame (O0OOO0O0O000O0OOO .main_frame ,bg ="white")#line:3194
        O0OOO0O0O000O0OOO .left_frame .grid (row =0 ,column =0 ,columnspan =2 ,sticky ="NEWS")#line:3195
        O0OOO0O0O000O0OOO .left_frame .grid_columnconfigure (0 ,weight =1 )#line:3196
        for O0O000O0O0O00OO0O in range (5 ):#line:3197
            O0OOO0O0O000O0OOO .left_frame .grid_rowconfigure (O0O000O0O0O00OO0O ,weight =1 ,uniform ="foo")#line:3198
        O0OOO0O0O000O0OOO .right_frame =tk .Frame (O0OOO0O0O000O0OOO .main_frame ,bg ="white")#line:3200
        O0OOO0O0O000O0OOO .right_frame .grid (row =0 ,column =2 ,columnspan =1 ,sticky ="NEWS")#line:3201
        O0OOO0O0O000O0OOO .right_frame .grid_columnconfigure (0 ,weight =1 )#line:3202
        for O0O000O0O0O00OO0O in range (5 ):#line:3203
            O0OOO0O0O000O0OOO .right_frame .grid_rowconfigure (O0O000O0O0O00OO0O ,weight =1 ,uniform ="foo")#line:3204
        O0OOOOOO0O0OO00OO =tk .PhotoImage (file =os .path .join (O0OOO0O0O000O0OOO .welcome_screen_006_dir ))#line:3207
        O0OOO0O0O000O0OOO .navbar_container =tk .Frame (O0OOO0O0O000O0OOO .left_frame ,bg ="white")#line:3208
        O0OOO0O0O000O0OOO .navbar_container .grid (row =0 ,column =0 ,sticky ="NEWS")#line:3209
        O0OOO0O0O000O0OOO .navbar_container .grid_columnconfigure (0 ,weight =1 )#line:3210
        for O0O000O0O0O00OO0O in range (2 ):#line:3211
            O0OOO0O0O000O0OOO .navbar_container .grid_rowconfigure (O0O000O0O0O00OO0O ,weight =1 ,uniform ="foo")#line:3212
        O0OOO0O0O000O0OOO .welcome_screen_006_image =O0OOO0O0O000O0OOO .resize (O0OOOOOO0O0OO00OO ,200 ,59 )#line:3214
        O0OOO0O0O000O0OOO .welcome_screen_006_bg =tk .Label (O0OOO0O0O000O0OOO .navbar_container ,image =O0OOO0O0O000O0OOO .welcome_screen_006_image ,bg ="white")#line:3215
        O0OOO0O0O000O0OOO .welcome_screen_006_bg .grid (row =0 ,column =0 ,sticky ="NW")#line:3216
        O0OOO0O0O000O0OOO .navbar_menu_container =tk .Label (O0OOO0O0O000O0OOO .navbar_container ,bg ="white")#line:3218
        O0OOO0O0O000O0OOO .navbar_menu_container .grid (row =1 ,column =0 ,sticky ="NW")#line:3219
        O0OOO0O0O000O0OOO .welcome_screen_header =tk .Label (O0OOO0O0O000O0OOO .left_frame ,text ="Welcome to SnapEDA",bg ="white",font =("Open Sans","32","bold"))#line:3221
        O0OOO0O0O000O0OOO .welcome_screen_header .grid (row =1 ,column =0 ,rowspan =1 ,sticky ="SEW")#line:3222
        OOOO0O0OOO0000000 =tk .PhotoImage (file =os .path .join (O0OOO0O0O000O0OOO .welcome_screen_001_dir ))#line:3224
        O0OOO0O0O000O0OOO .welcome_screen_001_image =O0OOO0O0O000O0OOO .resize (OOOO0O0OOO0000000 ,297 ,333 )#line:3225
        O0OOO0O0O000O0OOO .welcome_screen_001_bg =tk .Label (O0OOO0O0O000O0OOO .right_frame ,image =O0OOO0O0O000O0OOO .welcome_screen_001_image ,bg ="white")#line:3226
        O0OOO0O0O000O0OOO .welcome_screen_001_bg .grid (row =0 ,column =0 ,sticky ="NE",rowspan =3 )#line:3227
        O0OO00OO0O0OO00OO =tk .PhotoImage (file =os .path .join (O0OOO0O0O000O0OOO .welcome_screen_005_dir ))#line:3229
        O0OOO0O0O000O0OOO .welcome_screen_005_image =O0OOO0O0O000O0OOO .resize (O0OO00OO0O0OO00OO ,267 ,72 )#line:3230
        O0OOO0O0O000O0OOO .welcome_screen_005_bg =tk .Label (O0OOO0O0O000O0OOO .right_frame ,image =O0OOO0O0O000O0OOO .welcome_screen_005_image ,bg ="white")#line:3231
        O0OOO0O0O000O0OOO .welcome_screen_005_bg .grid (row =4 ,column =0 ,rowspan =1 ,sticky ="SE")#line:3232
        O0OOO0O0O000O0OOO .welcome_container =tk .Frame (O0OOO0O0O000O0OOO .left_frame ,bg ="white")#line:3235
        O0OOO0O0O000O0OOO .welcome_container .grid (row =2 ,column =0 ,rowspan =2 ,sticky ="NEWS")#line:3236
        O0OOO0O0O000O0OOO .welcome_container .grid_columnconfigure (0 ,weight =1 )#line:3237
        for O0O000O0O0O00OO0O in range (5 ):#line:3238
            O0OOO0O0O000O0OOO .welcome_container .grid_rowconfigure (O0O000O0O0O00OO0O ,weight =1 ,uniform ="foo")#line:3239
        O0OOO0O0O000O0OOO .welcome_screen_subheader =tk .Label (O0OOO0O0O000O0OOO .welcome_container ,text ="Let's make your your design a snap. Download ready-to-use\nPCB footprints, schematic symbols, and 3D models.",bg ="white",font =("Open Sans","12"),justify =tk .LEFT )#line:3241
        O0OOO0O0O000O0OOO .welcome_screen_subheader .grid (row =0 ,column =0 ,rowspan =1 ,sticky ="NEWS")#line:3242
        O0OOO0O0O000O0OOO .welcome_screen_search_container =tk .Frame (O0OOO0O0O000O0OOO .welcome_container ,bg ="white")#line:3244
        O0OOO0O0O000O0OOO .welcome_screen_search_container .grid (row =1 ,column =0 ,rowspan =1 ,sticky ="NEW",padx =(40 ,40 ),pady =(20 ,0 ))#line:3245
        O0OOO0O0O000O0OOO .welcome_screen_search_container .grid_columnconfigure (0 ,weight =1 )#line:3246
        O0OOO0O0O000O0OOO .welcome_screen_search_container .grid_rowconfigure (0 ,weight =1 )#line:3247
        tk .Label (O0OOO0O0O000O0OOO .welcome_screen_search_container ,bg ="#E1E1E1").grid (row =0 ,column =0 ,sticky ="NEWS")#line:3249
        tk .Label (O0OOO0O0O000O0OOO .welcome_screen_search_container ,bg ="white").grid (row =0 ,column =0 ,sticky ="NEWS",padx =(1 ,1 ),pady =(1 ,1 ))#line:3250
        O0OOO0O0O000O0OOO .search_bar =tk .Entry (O0OOO0O0O000O0OOO .welcome_screen_search_container ,fg ="#696969",bg ="white",font =("Open Sans",13 ),borderwidth =0 ,highlightthickness =0 )#line:3251
        O0OOO0O0O000O0OOO .search_bar .grid (row =0 ,column =0 ,sticky ="NEWS",padx =(25 ,25 ),pady =(1 ,1 ))#line:3252
        O0OOO0O0O000O0OOO .welcome_screen_search_button_im =tk .PhotoImage (file =os .path .join (O0OOO0O0O000O0OOO .appdata_dir ,"4i2efbui.png"))#line:3254
        O0OOO0O0O000O0OOO .welcome_screen_search_button_image =O0OOO0O0O000O0OOO .resize (O0OOO0O0O000O0OOO .welcome_screen_search_button_im ,73 ,55 )#line:3255
        O0OOO0O0O000O0OOO .welcome_screen_button =tk .Label (O0OOO0O0O000O0OOO .welcome_screen_search_container ,height =50 ,bg ="#ff761a",text ="",image =O0OOO0O0O000O0OOO .welcome_screen_search_button_image ,cursor ="hand2")#line:3256
        O0OOO0O0O000O0OOO .welcome_screen_button .grid (row =0 ,column =0 ,sticky ="NE",padx =(0 ,0 ),pady =(0 ,0 ))#line:3257
        O0OOO0O0O000O0OOO .welcome_screen_button .bind ("<Button-1>",O0OOO0O0O000O0OOO .welcome_screen_search_callback )#line:3258
        O0OOO0O0O000O0OOO .search_bar .bind ('<Return>',O0OOO0O0O000O0OOO .welcome_screen_search_callback )#line:3259
        O0OOO0O0O000O0OOO .search_bar .bind ('<Button-3>',O0OOO0O0O000O0OOO .show_copy_paste_option )#line:3260
        O0OOO0O0O000O0OOO .example_frame =tk .Frame (O0OOO0O0O000O0OOO .welcome_container ,bg ="white")#line:3262
        O0OOO0O0O000O0OOO .example_frame .grid (row =2 ,column =0 ,columnspan =1 ,sticky ="NW",padx =(25 ,0 ),pady =(25 ,0 ))#line:3263
        for O0O000O0O0O00OO0O in range (3 ):#line:3264
            O0OOO0O0O000O0OOO .example_frame .grid_columnconfigure (O0O000O0O0O00OO0O ,weight =1 ,uniform ="foo")#line:3265
        O0OOO0O0O000O0OOO .example_frame .grid_rowconfigure (0 ,weight =1 )#line:3266
        O0OOO0O0O000O0OOO .see_example_label =tk .Label (O0OOO0O0O000O0OOO .example_frame ,text ="Or see examples",bg ="white",font =("Open Sans","10","bold"))#line:3268
        O0OOO0O0O000O0OOO .see_example_label .grid (row =0 ,column =0 )#line:3269
        O0OOO0O0O000O0OOO .usb_type_c_button_im =tk .PhotoImage (file =O0OOO0O0O000O0OOO .usb_type_c_button_dir )#line:3271
        O0OOO0O0O000O0OOO .usb_type_c_button_image =O0OOO0O0O000O0OOO .resize (O0OOO0O0O000O0OOO .usb_type_c_button_im ,89 ,21 )#line:3272
        O0OOO0O0O000O0OOO .usb_type_c_button =tk .Label (O0OOO0O0O000O0OOO .example_frame ,bg ="white",text ="",image =O0OOO0O0O000O0OOO .usb_type_c_button_image ,cursor ="hand2")#line:3273
        O0OOO0O0O000O0OOO .usb_type_c_button .grid (row =0 ,column =1 ,padx =(0 ,0 ),pady =(0 ,0 ))#line:3274
        O0OOO0O0O000O0OOO .usb_type_c_button .bind ('<Button-1>',O0OOO0O0O000O0OOO .usb_type_c_button_callback )#line:3275
        O0OOO0O0O000O0OOO .microcontroller_button_im =tk .PhotoImage (file =O0OOO0O0O000O0OOO .microcontroller_button_dir )#line:3277
        O0OOO0O0O000O0OOO .microcontroller_button_image =O0OOO0O0O000O0OOO .resize (O0OOO0O0O000O0OOO .microcontroller_button_im ,89 ,21 )#line:3278
        O0OOO0O0O000O0OOO .microcontroller_button =tk .Label (O0OOO0O0O000O0OOO .example_frame ,bg ="white",text ="",image =O0OOO0O0O000O0OOO .microcontroller_button_image ,cursor ="hand2")#line:3279
        O0OOO0O0O000O0OOO .microcontroller_button .grid (row =0 ,column =2 ,padx =(0 ,0 ),pady =(0 ,0 ))#line:3280
        O0OOO0O0O000O0OOO .microcontroller_button .bind ('<Button-1>',O0OOO0O0O000O0OOO .microcontroller_button_callback )#line:3281
        O0OOO0O0O000O0OOO .left_003_frame =tk .Frame (O0OOO0O0O000O0OOO .left_frame ,bg ="white")#line:3283
        O0OOO0O0O000O0OOO .left_003_frame .grid (row =3 ,column =0 ,rowspan =2 ,sticky ="NEWS",pady =(70 ,0 ))#line:3284
        for O0O000O0O0O00OO0O in range (3 ):#line:3285
            O0OOO0O0O000O0OOO .left_003_frame .grid_columnconfigure (O0O000O0O0O00OO0O ,weight =1 ,uniform ="foo")#line:3286
        for O0O000O0O0O00OO0O in range (2 ):#line:3287
            O0OOO0O0O000O0OOO .left_003_frame .grid_rowconfigure (O0O000O0O0O00OO0O ,weight =1 )#line:3288
        O0O00OO00O0OOOO0O =tk .PhotoImage (file =os .path .join (O0OOO0O0O000O0OOO .welcome_screen_002_dir ))#line:3291
        O0OOO0O0O000O0OOO .welcome_screen_002_image =O0OOO0O0O000O0OOO .resize (O0O00OO00O0OOOO0O ,100 ,113 )#line:3292
        O0OOO0O0O000O0OOO .welcome_screen_002_bg =tk .Label (O0OOO0O0O000O0OOO .left_003_frame ,image =O0OOO0O0O000O0OOO .welcome_screen_002_image ,bg ="white")#line:3293
        O0OOO0O0O000O0OOO .welcome_screen_002_bg .grid (row =0 ,column =0 ,padx =(30 ,25 ),sticky ="S")#line:3294
        O0OOO0O0O000O0OOO .label_001 =tk .Label (O0OOO0O0O000O0OOO .left_003_frame ,text ="Focus on Design",bg ="white",font =("Open Sans","10","bold"))#line:3296
        O0OOO0O0O000O0OOO .label_001 .grid (row =1 ,column =0 ,padx =(30 ,25 ),sticky ="N")#line:3297
        O00O00O00O0O0OO00 =tk .PhotoImage (file =os .path .join (O0OOO0O0O000O0OOO .welcome_screen_003_dir ))#line:3299
        O0OOO0O0O000O0OOO .welcome_screen_003_image =O0OOO0O0O000O0OOO .resize (O00O00O00O0O0OO00 ,100 ,113 )#line:3300
        O0OOO0O0O000O0OOO .welcome_screen_003_bg =tk .Label (O0OOO0O0O000O0OOO .left_003_frame ,image =O0OOO0O0O000O0OOO .welcome_screen_003_image ,bg ="white")#line:3301
        O0OOO0O0O000O0OOO .welcome_screen_003_bg .grid (row =0 ,column =1 ,padx =(25 ,25 ),sticky ="S")#line:3302
        O0OOO0O0O000O0OOO .label_002 =tk .Label (O0OOO0O0O000O0OOO .left_003_frame ,text ="Crush Deadlines",bg ="white",font =("Open Sans","10","bold"))#line:3304
        O0OOO0O0O000O0OOO .label_002 .grid (row =1 ,column =1 ,padx =(30 ,25 ),sticky ="N")#line:3305
        OOO0O00O0OO000O00 =tk .PhotoImage (file =os .path .join (O0OOO0O0O000O0OOO .welcome_screen_004_dir ))#line:3307
        O0OOO0O0O000O0OOO .welcome_screen_004_image =O0OOO0O0O000O0OOO .resize (OOO0O00O0OO000O00 ,100 ,113 )#line:3308
        O0OOO0O0O000O0OOO .welcome_screen_004_bg =tk .Label (O0OOO0O0O000O0OOO .left_003_frame ,image =O0OOO0O0O000O0OOO .welcome_screen_004_image ,bg ="white")#line:3309
        O0OOO0O0O000O0OOO .welcome_screen_004_bg .grid (row =0 ,column =2 ,padx =(25 ,30 ),sticky ="S")#line:3310
        O0OOO0O0O000O0OOO .label_003 =tk .Label (O0OOO0O0O000O0OOO .left_003_frame ,text ="Prevent Errors",bg ="white",font =("Open Sans","10","bold"))#line:3312
        O0OOO0O0O000O0OOO .label_003 .grid (row =1 ,column =2 ,padx =(30 ,25 ),sticky ="N")#line:3313
        O0OOO0O0O000O0OOO .settings_menu_img =tk .PhotoImage (file =O0OOO0O0O000O0OOO .settings_menu_img_dir )#line:3316
        O0OOO0O0O000O0OOO .how_it_works_menu_img =tk .PhotoImage (file =O0OOO0O0O000O0OOO .how_it_works_menu_img_dir )#line:3317
        O0OOO0O0O000O0OOO .update_menu_img =tk .PhotoImage (file =O0OOO0O0O000O0OOO .update_menu_img_dir )#line:3318
        O0OOO0O0O000O0OOO .info_menu_img =tk .PhotoImage (file =O0OOO0O0O000O0OOO .info_menu_img_dir )#line:3319
        O0OOO0O0O000O0OOO .how_it_works_button =tk .Label (O0OOO0O0O000O0OOO .navbar_menu_container ,fg ="#FF761B",bg ="white",image =O0OOO0O0O000O0OOO .how_it_works_menu_img ,text ="How it works",cursor ="hand2",font =("Open Sans","8","bold","underline"))#line:3322
        O0OOO0O0O000O0OOO .update_button =tk .Label (O0OOO0O0O000O0OOO .navbar_menu_container ,fg ="#FF761B",bg ="white",image =O0OOO0O0O000O0OOO .update_menu_img ,text ="Update",cursor ="hand2",font =("Open Sans","8","bold","underline"))#line:3323
        O0OOO0O0O000O0OOO .help_me_button =tk .Label (O0OOO0O0O000O0OOO .navbar_menu_container ,fg ="#FF761B",bg ="white",image =O0OOO0O0O000O0OOO .info_menu_img ,text ="Help Me",cursor ="hand2",font =("Open Sans","8","bold","underline"))#line:3324
        O0OOO0O0O000O0OOO .how_it_works_button .bind ("<Button-1>",O0OOO0O0O000O0OOO .setting_callback )#line:3327
        O0OOO0O0O000O0OOO .update_button .bind ("<Button-1>",O0OOO0O0O000O0OOO .update_callback )#line:3328
        O0OOO0O0O000O0OOO .help_me_button .bind ("<Button-1>",O0OOO0O0O000O0OOO .how_it_works_callback )#line:3329
        O0OOO0O0O000O0OOO .help_me_button .grid (row =0 ,column =2 ,padx =(0 ,0 ),sticky ="W")#line:3331
        O0OOO0O0O000O0OOO .update_button .grid (row =0 ,column =1 ,padx =(0 ,15 ),sticky ="W")#line:3332
        O0OOO0O0O000O0OOO .how_it_works_button .grid (row =0 ,column =0 ,padx =(10 ,15 ),sticky ="W")#line:3333
class LoginScreen (tk .Frame ):#line:3337
    ""#line:3343
    def __init__ (OOOOO0O00000OO000 ,OOO0000OOOOOOO0OO ):#line:3345
        tk .Frame .__init__ (OOOOO0O00000OO000 ,OOO0000OOOOOOO0OO )#line:3346
        OOOOO0O00000OO000 .parent =OOO0000OOOOOOO0OO #line:3347
        OOOOO0O00000OO000 .parent .geometry (CONST_LOGIN_GEOMETRY )#line:3348
        OOOOO0O00000OO000 .parent .minsize (width =CONST_LOGIN_WINDOW_WIDTH ,height =CONST_LOGIN_GEOMETRY_HEIGHT )#line:3349
        OOOOO0O00000OO000 .dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:3352
        OOOOO0O00000OO000 .is_mac =platform .mac_ver ()[0 ]!=""#line:3365
        OOOOO0O00000OO000 .is_windows =(os .name =='nt')#line:3366
        O000O0OO0OOO0O0OO =''#line:3367
        try :#line:3368
            if OOOOO0O00000OO000 .is_windows :#line:3369
                OOOOO0O00000OO000 .windata_dir =os .path .join (os .getenv ('HOMEDRIVE'),os .getenv ('HOMEPATH'),"SnapEDA Kicad Plugin")#line:3372
                OOOOO0O00000OO000 .appdata_dir =os .path .join (OOOOO0O00000OO000 .windata_dir ,"App")#line:3373
                with open (os .path .join (OOOOO0O00000OO000 .appdata_dir ,".token"),"r")as O00000000000O00O0 :#line:3374
                    O000O0OO0OOO0O0OO =str (O00000000000O00O0 .readline ())#line:3375
                    O00000000000O00O0 .close ()#line:3376
            elif OOOOO0O00000OO000 .is_mac :#line:3377
                OOOOO0O00000OO000 .macdata_dir =os .path .join (os .path .expanduser ("~"),"Documents","SnapEDA Kicad Plugin")#line:3378
                OOOOO0O00000OO000 .appdata_dir =os .path .join (OOOOO0O00000OO000 .macdata_dir ,"App")#line:3379
                with open (os .path .join (OOOOO0O00000OO000 .appdata_dir ,".token"),"r")as O00000000000O00O0 :#line:3380
                    O000O0OO0OOO0O0OO =str (O00000000000O00O0 .readline ())#line:3381
                    O00000000000O00O0 .close ()#line:3382
            else :#line:3383
                OOOOO0O00000OO000 .dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:3384
                with open (os .path .join (OOOOO0O00000OO000 .dir_path ,".token"),"r")as O00000000000O00O0 :#line:3385
                    O000O0OO0OOO0O0OO =str (O00000000000O00O0 .readline ())#line:3386
                    O00000000000O00O0 .close ()#line:3387
        except :#line:3388
            O000O0OO0OOO0O0OO =''#line:3389
        try :#line:3391
            O0O0O0OO00O00OOOO ={'User-Agent':"Kicad"}#line:3392
            O0O0O0000OO00OOO0 ="https://www.snapeda.com/api/v1/parts/search?q=%s&token=%s"%("test-search",O000O0OO0OOO0O0OO )#line:3393
            if sys .version_info [0 ]==3 :#line:3395
                O00OO0OOO0O00OOOO =urllib .request .Request (O0O0O0000OO00OOO0 ,headers =O0O0O0OO00O00OOOO )#line:3396
                OOO0OOOOO0O0OO0OO =urllib .request .urlopen (O00OO0OOO0O00OOOO ,timeout =5 ).read ()#line:3397
            else :#line:3398
                O00OO0OOO0O00OOOO =urllib2 .Request (O0O0O0000OO00OOO0 ,headers =O0O0O0OO00O00OOOO )#line:3399
                OOO0OOOOO0O0OO0OO =urllib2 .urlopen (O00OO0OOO0O00OOOO ,timeout =5 ).read ()#line:3400
            O000O0OO00000OOOO =json .loads (OOO0OOOOO0O0OO0OO )#line:3401
            if (O000O0OO00000OOOO ['error']==None ):#line:3402
                for O0OO0OOOO00OOOOOO in range (5 ):#line:3403
                    for OOO0OO000OOOO0O0O in OOOOO0O00000OO000 .parent .grid_slaves (row =O0OO0OOOO00OOOOOO ,column =0 ):#line:3404
                        OOO0OO000OOOO0O0O .destroy ()#line:3405
                WelcomeScreen (OOOOO0O00000OO000 .parent )#line:3406
                return #line:3407
        except :#line:3408
            pass #line:3409
        if OOOOO0O00000OO000 .is_windows :#line:3412
            OOOOO0O00000OO000 .windata_dir =os .path .join (os .getenv ('HOMEDRIVE'),os .getenv ('HOMEPATH'),"SnapEDA Kicad Plugin")#line:3415
            OOOOO0O00000OO000 .appdata_dir =os .path .join (OOOOO0O00000OO000 .windata_dir ,"App")#line:3416
            OOOOO0O00000OO000 .flip_table_dir =os .path .join (os .getenv ('APPDATA'),'kicad','fp-lib-table')#line:3419
            OOOOO0O00000OO000 .kicad_common_dir =os .path .join (os .getenv ('APPDATA'),'kicad','kicad_common')#line:3422
            OOOOO0O00000OO000 .kicad_library_dir =os .path .join (OOOOO0O00000OO000 .windata_dir ,'KiCad Library')#line:3423
            OOOOO0O00000OO000 .snapeda_library_dir =os .path .join (OOOOO0O00000OO000 .kicad_library_dir ,'SnapEDA Library')#line:3426
            OOOOO0O00000OO000 .snapeda_library_abs_dir =os .path .join (OOOOO0O00000OO000 .kicad_library_dir ,'SnapEDA Library.pretty')#line:3428
            if not os .path .exists (OOOOO0O00000OO000 .windata_dir ):#line:3430
                os .makedirs (OOOOO0O00000OO000 .windata_dir )#line:3431
            if not os .path .exists (OOOOO0O00000OO000 .appdata_dir ):#line:3432
                os .makedirs (OOOOO0O00000OO000 .appdata_dir )#line:3433
            if not os .path .exists (OOOOO0O00000OO000 .kicad_library_dir ):#line:3434
                os .makedirs (OOOOO0O00000OO000 .kicad_library_dir )#line:3435
            if not os .path .exists (OOOOO0O00000OO000 .snapeda_library_dir ):#line:3436
                os .makedirs (OOOOO0O00000OO000 .snapeda_library_dir )#line:3437
            if not os .path .exists (OOOOO0O00000OO000 .snapeda_library_abs_dir ):#line:3438
                os .makedirs (OOOOO0O00000OO000 .snapeda_library_abs_dir )#line:3439
        elif OOOOO0O00000OO000 .is_mac :#line:3440
            OOOOO0O00000OO000 .macdata_dir =os .path .join (os .path .expanduser ("~"),"Documents","SnapEDA Kicad Plugin")#line:3441
            OOOOO0O00000OO000 .appdata_dir =os .path .join (OOOOO0O00000OO000 .macdata_dir ,"App")#line:3442
            OOOOO0O00000OO000 .flip_table_dir =os .path .join (os .getenv ('HOME'),'library','preferences','kicad','fp-lib-table')#line:3443
            OOOOO0O00000OO000 .kicad_common_dir =os .path .join (os .getenv ('HOME'),'library','preferences','kicad','kicad_common')#line:3444
            OOOOO0O00000OO000 .kicad_library_dir =os .path .join (OOOOO0O00000OO000 .macdata_dir ,'KiCad Library')#line:3445
            OOOOO0O00000OO000 .snapeda_library_dir =os .path .join (OOOOO0O00000OO000 .kicad_library_dir ,'SnapEDA Library')#line:3447
            OOOOO0O00000OO000 .snapeda_library_abs_dir =os .path .join (OOOOO0O00000OO000 .kicad_library_dir ,'SnapEDA Library.pretty')#line:3449
            if not os .path .exists (OOOOO0O00000OO000 .appdata_dir ):#line:3451
                os .makedirs (OOOOO0O00000OO000 .appdata_dir )#line:3452
            if not os .path .exists (OOOOO0O00000OO000 .kicad_library_dir ):#line:3453
                os .makedirs (OOOOO0O00000OO000 .kicad_library_dir )#line:3454
            if not os .path .exists (OOOOO0O00000OO000 .snapeda_library_dir ):#line:3455
                os .makedirs (OOOOO0O00000OO000 .snapeda_library_dir )#line:3456
            if not os .path .exists (OOOOO0O00000OO000 .snapeda_library_abs_dir ):#line:3457
                os .makedirs (OOOOO0O00000OO000 .snapeda_library_abs_dir )#line:3458
        else :#line:3459
            OOOOO0O00000OO000 .appdata_dir =os .path .join (OOOOO0O00000OO000 .dir_path ,"assets")#line:3460
            OOOOO0O00000OO000 .flip_table_dir =os .path .join (os .path .expanduser ("~"),'.config','kicad','fp-lib-table')#line:3464
            OOOOO0O00000OO000 .kicad_common_dir =os .path .join (os .path .expanduser ("~"),'.config','kicad','kicad_common')#line:3468
            O00000O0O0OO00O0O =os .path .expanduser ("~")#line:3469
            OOOOO0O00000OO000 .kicad_library_dir =os .path .join (O00000O0O0OO00O0O ,'KiCad Library')#line:3470
            OOOOO0O00000OO000 .snapeda_library_dir =os .path .join (OOOOO0O00000OO000 .kicad_library_dir ,'SnapEDA Library')#line:3472
            OOOOO0O00000OO000 .snapeda_library_abs_dir =os .path .join (OOOOO0O00000OO000 .kicad_library_dir ,'SnapEDA Library.pretty')#line:3474
            if not os .path .exists (OOOOO0O00000OO000 .appdata_dir ):#line:3475
                os .makedirs (OOOOO0O00000OO000 .appdata_dir )#line:3476
            if not os .path .exists (OOOOO0O00000OO000 .kicad_library_dir ):#line:3477
                os .makedirs (OOOOO0O00000OO000 .kicad_library_dir )#line:3478
            if not os .path .exists (OOOOO0O00000OO000 .snapeda_library_dir ):#line:3479
                os .makedirs (OOOOO0O00000OO000 .snapeda_library_dir )#line:3480
            if not os .path .exists (OOOOO0O00000OO000 .snapeda_library_abs_dir ):#line:3481
                os .makedirs (OOOOO0O00000OO000 .snapeda_library_abs_dir )#line:3482
        OOOOO0O00000OO000 .login_bg_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"Group+292.png")#line:3484
        OOOOO0O00000OO000 .username_bg_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"3xm843ff.png")#line:3485
        OOOOO0O00000OO000 .password_bg_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"ek8owdjt.png")#line:3486
        OOOOO0O00000OO000 .login_button_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"g4pik2y2.png")#line:3487
        OOOOO0O00000OO000 .logo_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"lkeixquo.png")#line:3488
        OOOOO0O00000OO000 .loading_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"jwhk6qck.gif")#line:3489
        OOOOO0O00000OO000 .cover_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"RefDesign.png")#line:3490
        OOOOO0O00000OO000 .symbol_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"Symbol.png")#line:3491
        OOOOO0O00000OO000 .package_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"Footprint.png")#line:3493
        if not os .path .exists (OOOOO0O00000OO000 .logo_image_dir ):#line:3494
            tkMessageBox .showwarning ("Installation","Installation is started, please click OK and wait for the complete."+"It may take a time, login screen will be opened when the installation is completed."+"After the installation is completed, you have to restart the plugin, Pcbnew and KiCad.")#line:3497
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/lkeixquo.png")#line:3498
        if not os .path .exists (OOOOO0O00000OO000 .loading_image_dir ):#line:3500
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/jwhk6qck.gif")#line:3501
        if not os .path .exists (OOOOO0O00000OO000 .cover_image_dir ):#line:3502
            OOOOO0O00000OO000 .download_image ("https://s3.amazonaws.com/snapeda/ulp/RefDesign.png")#line:3504
        if not os .path .exists (OOOOO0O00000OO000 .symbol_image_dir ):#line:3505
            OOOOO0O00000OO000 .download_image ("https://s3.amazonaws.com/snapeda/ulp/Symbol.png")#line:3507
        if not os .path .exists (OOOOO0O00000OO000 .package_image_dir ):#line:3508
            OOOOO0O00000OO000 .download_image ("https://s3.amazonaws.com/snapeda/ulp/Footprint.png")#line:3510
        if not os .path .exists (OOOOO0O00000OO000 .login_bg_image_dir ):#line:3511
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/Group+292.png")#line:3513
        if not os .path .exists (OOOOO0O00000OO000 .username_bg_image_dir ):#line:3514
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/3xm843ff.png")#line:3516
        if not os .path .exists (OOOOO0O00000OO000 .password_bg_image_dir ):#line:3517
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/ek8owdjt.png")#line:3519
        if not os .path .exists (OOOOO0O00000OO000 .login_button_image_dir ):#line:3520
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/g4pik2y2.png")#line:3522
        OOOOO0O00000OO000 .welcome_screen_001_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"Mask+Group.png")#line:3525
        OOOOO0O00000OO000 .welcome_screen_002_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"icon1.bbe45f7648f7.png")#line:3526
        OOOOO0O00000OO000 .welcome_screen_003_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"ico_deadlines.8ba69c3f942a.png")#line:3527
        OOOOO0O00000OO000 .welcome_screen_004_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"icon2.924b03ebfccc.png")#line:3528
        OOOOO0O00000OO000 .welcome_screen_005_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"powered+by+snapEDA.png")#line:3529
        OOOOO0O00000OO000 .welcome_screen_006_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"snapeda-transparent.png")#line:3530
        OOOOO0O00000OO000 .usb_type_c_button_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"usb+type+c.png")#line:3531
        OOOOO0O00000OO000 .microcontroller_button_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"usb+microcontroller.png")#line:3532
        if not os .path .exists (OOOOO0O00000OO000 .welcome_screen_001_dir ):#line:3534
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Designs+-+API/Mask+Group.png")#line:3536
        if not os .path .exists (OOOOO0O00000OO000 .welcome_screen_002_dir ):#line:3537
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/icon1.bbe45f7648f7.png")#line:3539
        if not os .path .exists (OOOOO0O00000OO000 .welcome_screen_003_dir ):#line:3540
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/ico_deadlines.8ba69c3f942a.png")#line:3542
        if not os .path .exists (OOOOO0O00000OO000 .welcome_screen_004_dir ):#line:3543
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/icon2.924b03ebfccc.png")#line:3545
        if not os .path .exists (OOOOO0O00000OO000 .welcome_screen_005_dir ):#line:3546
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Designs+-+API/powered+by+snapEDA.png")#line:3548
        if not os .path .exists (OOOOO0O00000OO000 .welcome_screen_006_dir ):#line:3549
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/snapeda-transparent.png")#line:3551
        if not os .path .exists (OOOOO0O00000OO000 .usb_type_c_button_dir ):#line:3552
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/usb+type+c.png")#line:3554
        if not os .path .exists (OOOOO0O00000OO000 .microcontroller_button_dir ):#line:3555
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/usb+microcontroller.png")#line:3557
        OOOOO0O00000OO000 .filter_button_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"neeo2s8g.png")#line:3559
        OOOOO0O00000OO000 .settings_button_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"7svfoe57.png")#line:3560
        OOOOO0O00000OO000 .about_button_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"2kdtezsl.png")#line:3561
        OOOOO0O00000OO000 .passive_components_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"t3gwhnzh.png")#line:3562
        OOOOO0O00000OO000 .all_button_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"dsyrvfl9.png")#line:3563
        OOOOO0O00000OO000 .powered_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"orb6glbv.png")#line:3564
        OOOOO0O00000OO000 .datasheet_button_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"oxfarxz8.png")#line:3565
        OOOOO0O00000OO000 .datasheet_available_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"m4lamm2w.png")#line:3566
        OOOOO0O00000OO000 .datasheet_not_available_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"4cnn9kkf.png")#line:3567
        OOOOO0O00000OO000 .symbol_available_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"huaxvbtm.png")#line:3568
        OOOOO0O00000OO000 .symbol_not_available_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"tmuhgmxh.png")#line:3569
        OOOOO0O00000OO000 .footprint_available_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"3ruuehki.png")#line:3570
        OOOOO0O00000OO000 .footprint_not_available_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"footprint_outline.cebd715affd8.png")#line:3571
        OOOOO0O00000OO000 .available_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"uku4ceuv.png")#line:3572
        OOOOO0O00000OO000 .not_available_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"zah3n8r4.png")#line:3573
        OOOOO0O00000OO000 .prev_bg_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"iu2ma3jp.png")#line:3574
        OOOOO0O00000OO000 .next_bg_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"witafnjf.png")#line:3575
        OOOOO0O00000OO000 .selected_page_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"izif2qd8.png")#line:3576
        OOOOO0O00000OO000 .download_button_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"download+orange.png")#line:3577
        OOOOO0O00000OO000 .view_button_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"viewonsnapeda+white.png")#line:3578
        OOOOO0O00000OO000 .search_button_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"4i2efbui.png")#line:3579
        OOOOO0O00000OO000 .loading_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"jwhk6qck.gif")#line:3580
        OOOOO0O00000OO000 .icon_bitmap_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"32x32.ico")#line:3581
        if not os .path .exists (OOOOO0O00000OO000 .filter_button_image_dir ):#line:3582
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/neeo2s8g.png")#line:3583
        if not os .path .exists (OOOOO0O00000OO000 .settings_button_image_dir ):#line:3584
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/7svfoe57.png")#line:3585
        if not os .path .exists (OOOOO0O00000OO000 .about_button_image_dir ):#line:3586
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/2kdtezsl.png")#line:3587
        if not os .path .exists (OOOOO0O00000OO000 .passive_components_image_dir ):#line:3588
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/t3gwhnzh.png")#line:3589
        if not os .path .exists (OOOOO0O00000OO000 .all_button_image_dir ):#line:3590
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/dsyrvfl9.png")#line:3591
        if not os .path .exists (OOOOO0O00000OO000 .powered_image_dir ):#line:3592
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/orb6glbv.png")#line:3593
        if not os .path .exists (OOOOO0O00000OO000 .datasheet_button_dir ):#line:3594
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/oxfarxz8.png")#line:3595
        if not os .path .exists (OOOOO0O00000OO000 .datasheet_available_dir ):#line:3596
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/m4lamm2w.png")#line:3597
        if not os .path .exists (OOOOO0O00000OO000 .datasheet_not_available_dir ):#line:3598
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/4cnn9kkf.png")#line:3599
        if not os .path .exists (OOOOO0O00000OO000 .symbol_available_dir ):#line:3600
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/huaxvbtm.png")#line:3601
        if not os .path .exists (OOOOO0O00000OO000 .symbol_not_available_dir ):#line:3602
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/tmuhgmxh.png")#line:3603
        if not os .path .exists (OOOOO0O00000OO000 .footprint_available_dir ):#line:3604
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/3ruuehki.png")#line:3605
        if not os .path .exists (OOOOO0O00000OO000 .footprint_not_available_dir ):#line:3606
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/62r7iuz7.png")#line:3607
        if not os .path .exists (OOOOO0O00000OO000 .available_dir ):#line:3608
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/uku4ceuv.png")#line:3609
        if not os .path .exists (OOOOO0O00000OO000 .not_available_dir ):#line:3610
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/zah3n8r4.png")#line:3611
        if not os .path .exists (OOOOO0O00000OO000 .prev_bg_dir ):#line:3612
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/iu2ma3jp.png")#line:3613
        if not os .path .exists (OOOOO0O00000OO000 .next_bg_dir ):#line:3614
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/witafnjf.png")#line:3615
        if not os .path .exists (OOOOO0O00000OO000 .selected_page_dir ):#line:3616
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/izif2qd8.png")#line:3617
        if not os .path .exists (OOOOO0O00000OO000 .download_button_dir ):#line:3618
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/download+orange.png")#line:3619
        if not os .path .exists (OOOOO0O00000OO000 .view_button_dir ):#line:3620
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/viewonsnapeda+white.png")#line:3621
        if not os .path .exists (OOOOO0O00000OO000 .search_button_image_dir ):#line:3622
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/4i2efbui.png")#line:3623
        if not os .path .exists (OOOOO0O00000OO000 .icon_bitmap_dir ):#line:3624
            OOOOO0O00000OO000 .download_ico ("https://snapeda.s3.amazonaws.com/Kicadplugin/32x32.ico")#line:3625
        OOOOO0O00000OO000 .avatar_image_dir =os .path .join (OOOOO0O00000OO000 .appdata_dir ,"avatar1.png")#line:3627
        if not os .path .exists (OOOOO0O00000OO000 .avatar_image_dir ):#line:3628
            OOOOO0O00000OO000 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/avatar1.png")#line:3629
        OOOOO0O00000OO000 .parent .grid_columnconfigure (0 ,weight =1 )#line:3631
        print ('Login screen initialized.')#line:3642
        OOOOO0O00000OO000 .initialize_user_interface ()#line:3643
    def download_ico (OO0OOOO00O0O0O0O0 ,OOOOO0OOOOO00OO0O ):#line:3645
        if sys .version_info [0 ]==3 :#line:3646
            urllib .request .urlretrieve (OOOOO0OOOOO00OO0O ,OO0OOOO00O0O0O0O0 .icon_bitmap_dir )#line:3647
        else :#line:3648
            urllib .urlretrieve (OOOOO0OOOOO00OO0O ,OO0OOOO00O0O0O0O0 .icon_bitmap_dir )#line:3649
    def download_image (O00OOO00OOOO0OO0O ,OOOOOO000OOO0OO00 ):#line:3651
        O00OO0O0O0000OOOO =OOOOOO000OOO0OO00 [OOOOOO000OOO0OO00 .rfind ('/')+1 :]#line:3653
        OOO00O0O0000O00O0 =os .path .join (O00OOO00OOOO0OO0O .appdata_dir ,O00OO0O0O0000OOOO )#line:3654
        O0OO0000OOO0O000O =OOO00O0O0000O00O0 [:-3 ]+"png"#line:3655
        if OOO00O0O0000O00O0 [-3 :]=="gif"or OOO00O0O0000O00O0 [-3 :]=="GIF":#line:3656
            O0OO0000OOO0O000O =OOO00O0O0000O00O0 #line:3657
        if not os .path .exists (O0OO0000OOO0O000O )and not O00OOO00OOOO0OO0O .is_mac :#line:3658
            if O00OOO00OOOO0OO0O .is_windows :#line:3659
                O0OOO00000O0O0O00 =os .path .join (os .path .dirname (__file__ ),"imagemagick","convert")#line:3660
                subprocess .check_call ([O0OOO00000O0O0O00 ,OOOOOO000OOO0OO00 .replace ("https","http"),O0OO0000OOO0O000O ],shell =True )#line:3661
            else :#line:3662
                subprocess .call ("convert "+OOOOOO000OOO0OO00 .replace ("https","http")+" "+O0OO0000OOO0O000O ,shell =True )#line:3663
        if O00OOO00OOOO0OO0O .is_mac :#line:3664
            if not os .path .exists (O0OO0000OOO0O000O ):#line:3665
                with open (OOO00O0O0000O00O0 ,"wb")as OO0O000O0O0O000O0 :#line:3666
                    if sys .version_info [0 ]==3 :#line:3667
                        OO0O00O0O0O0OOOO0 =urllib .request .urlopen (OOOOOO000OOO0OO00 ).read ()#line:3668
                    else :#line:3669
                        OO0O00O0O0O0OOOO0 =urllib2 .urlopen (OOOOOO000OOO0OO00 ).read ()#line:3670
                    OO0O000O0O0O000O0 .write (OO0O00O0O0O0OOOO0 )#line:3671
                    OO0O000O0O0O000O0 .close ()#line:3672
                    subprocess .check_call (["sips","-s","format","gif","%s"%OOO00O0O0000O00O0 ,"--out","%s"%O0OO0000OOO0O000O ],shell =True )#line:3673
        return O0OO0000OOO0O000O #line:3674
    def on_entry_click_username (O0O0O000O0O0O000O ,OO0O00O0O0O0OO0OO ):#line:3677
        if O0O0O000O0O0O000O .username_entry .get ()=="Username or Email":#line:3678
            O0O0O000O0O0O000O .username_entry .delete (0 ,"end")#line:3679
            O0O0O000O0O0O000O .username_entry .insert (0 ,'')#line:3680
            O0O0O000O0O0O000O .username_entry .config (fg ='black')#line:3681
    def on_focusout_username (OO0000000O00O0O00 ,O0O0O0OO0OOO00000 ):#line:3683
        if OO0000000O00O0O00 .username_entry .get ()=='':#line:3684
            OO0000000O00O0O00 .username_entry .insert (0 ,"Username or Email")#line:3685
            OO0000000O00O0O00 .username_entry .config (fg ='black')#line:3686
    def on_entry_click_password (OO00OOO0O0OO0OO0O ,O0000OOOOOOOO0O00 ):#line:3688
        if OO00OOO0O0OO0OO0O .password_entry .get ()=='Password':#line:3689
            OO00OOO0O0OO0OO0O .password_entry .delete (0 ,"end")#line:3690
            OO00OOO0O0OO0OO0O .password_entry .insert (0 ,'')#line:3691
            OO00OOO0O0OO0OO0O .password_entry .config (fg ='black',show ="*")#line:3692
    def on_focusout_password (OOOO0O00OOO000OO0 ,O0OOOO000O0OO00O0 ):#line:3694
        if OOOO0O00OOO000OO0 .password_entry .get ()=='':#line:3695
            OOOO0O00OOO000OO0 .password_entry .insert (0 ,'Password')#line:3696
            OOOO0O00OOO000OO0 .password_entry .config (fg ='black',show ="")#line:3697
    def check_login_thread (OOOO0OO0OOO0O0O0O ,OO0OOO000OOO00OO0 ):#line:3700
        OOOO0OO0OOO0O0O0O .login_button .config (state ="disabled",text ="")#line:3701
        OOOO0OO0OOO0O0O0O .login_thread =threading .Thread (target =OOOO0OO0OOO0O0O0O .check_login )#line:3702
        OOOO0OO0OOO0O0O0O .login_thread .start ()#line:3703
    def check_login (OOO0O0OO0O0OO00O0 ):#line:3705
        OOOO0O0O000OOOO0O ={'User-Agent':"Kicad"}#line:3706
        OO0O00OO0OO0000O0 ="https://www.snapeda.com/account/api-login/"#line:3707
        OO0O0OO0OO0000O0O ={'username':OOO0O0OO0O0OO00O0 .username_entry .get (),'password':OOO0O0OO0O0OO00O0 .password_entry .get (),'ref':"kicad-plugin",'plugin':'kicad'}#line:3713
        if sys .version_info [0 ]==3 :#line:3714
            OOOO0OOO0OO0O0O0O =urllib .parse .urlencode (OO0O0OO0OO0000O0O ).encode ("utf-8")#line:3715
            O0O00OO0O0O0O0OO0 =urllib .request .Request (OO0O00OO0OO0000O0 ,OOOO0OOO0OO0O0O0O ,headers =OOOO0O0O000OOOO0O )#line:3716
            O00O00O0OOO000OO0 =urllib .request .urlopen (O0O00OO0O0O0O0OO0 ).read ()#line:3717
        else :#line:3718
            OOOO0OOO0OO0O0O0O =urllib .urlencode (OO0O0OO0OO0000O0O )#line:3719
            O0O00OO0O0O0O0OO0 =urllib2 .Request (OO0O00OO0OO0000O0 ,OOOO0OOO0OO0O0O0O ,headers =OOOO0O0O000OOOO0O )#line:3720
            O00O00O0OOO000OO0 =urllib2 .urlopen (O0O00OO0O0O0O0OO0 ).read ()#line:3721
        OOO0O0OO0O0OO00O0 .data =json .loads (O00O00O0OOO000OO0 )#line:3722
        if OOO0O0OO0O0OO00O0 .data ["status"]=="logged_in":#line:3724
            if OOO0O0OO0O0OO00O0 .is_windows or OOO0O0OO0O0OO00O0 .is_mac :#line:3725
                O000OO0OO000O00O0 =os .path .join (OOO0O0OO0O0OO00O0 .appdata_dir ,"info.json")#line:3727
                with open (O000OO0OO000O00O0 )as O000OO0O0OOOO0OO0 :#line:3728
                    OOOO0OOO0OO0O0O0O =json .load (O000OO0O0OOOO0OO0 )#line:3729
                OOOO0OOO0OO0O0O0O ['username']=OOO0O0OO0O0OO00O0 .username_entry .get ()#line:3730
                OOOO0OOO0OO0O0O0O ['email']=OOO0O0OO0O0OO00O0 .data ['user_email']#line:3731
                with open (O000OO0OO000O00O0 ,'w')as O0OOOO000O0O0OO00 :#line:3732
                    json .dump (OOOO0OOO0OO0O0O0O ,O0OOOO000O0O0OO00 )#line:3733
                with open (os .path .join (OOO0O0OO0O0OO00O0 .appdata_dir ,".token"),"w")as OOOOOOOO0O00OOOO0 :#line:3735
                    OOOOOOOO0O00OOOO0 .write (OOO0O0OO0O0OO00O0 .data ["token"])#line:3736
                    OOOOOOOO0O00OOOO0 .close ()#line:3737
            else :#line:3738
                O000OO0OO000O00O0 =os .path .join (OOO0O0OO0O0OO00O0 .appdata_dir ,"info.json")#line:3740
                with open (O000OO0OO000O00O0 )as O000OO0O0OOOO0OO0 :#line:3741
                    OOOO0OOO0OO0O0O0O =json .load (O000OO0O0OOOO0OO0 )#line:3742
                OOOO0OOO0OO0O0O0O ['username']=OOO0O0OO0O0OO00O0 .username_entry .get ()#line:3743
                OOOO0OOO0OO0O0O0O ['email']=OOO0O0OO0O0OO00O0 .data ['user_email']#line:3744
                with open (O000OO0OO000O00O0 ,'w')as O0OOOO000O0O0OO00 :#line:3745
                    json .dump (OOOO0OOO0OO0O0O0O ,O0OOOO000O0O0OO00 )#line:3746
                with open (os .path .join (OOO0O0OO0O0OO00O0 .dir_path ,".token"),"w")as OOOOOOOO0O00OOOO0 :#line:3748
                    OOOOOOOO0O00OOOO0 .write (OOO0O0OO0O0OO00O0 .data ["token"])#line:3749
                    OOOOOOOO0O00OOOO0 .close ()#line:3750
            for OOOO000OOOOO0OO0O in range (5 ):#line:3752
                for O000OO00O00000OOO in OOO0O0OO0O0OO00O0 .parent .grid_slaves (row =OOOO000OOOOO0OO0O ,column =0 ):#line:3753
                    O000OO00O00000OOO .destroy ()#line:3754
            WelcomeScreen (OOO0O0OO0O0OO00O0 .parent )#line:3756
        else :#line:3757
            OOO0O0OO0O0OO00O0 .label .config (text ="The username/email or password you specified are not correct.")#line:3758
            OOO0O0OO0O0OO00O0 .login_button .config (state ="normal",text ="")#line:3759
    def resize (O0O000OO0O00O000O ,O0000O0O000O00O00 ,OOO000O00O00OOOOO ,O0OO00OO0000OOOO0 ):#line:3761
        ""#line:3765
        if sys .version_info [0 ]==3 :#line:3766
            OO0O0OOOO0OO0O00O =O0000O0O000O00O00 .width ()#line:3767
            O0OO0OO00000OOOO0 =O0000O0O000O00O00 .height ()#line:3768
            OOOOOO0O000000O00 =max (OO0O0OOOO0OO0O00O ,O0OO0OO00000OOOO0 )#line:3769
            O00OO00O00OOOO000 =max (OOO000O00O00OOOOO ,O0OO00OO0000OOOO0 )#line:3770
            if OOOOOO0O000000O00 >O00OO00O00OOOO000 :#line:3771
                return O0000O0O000O00O00 .subsample (int (OOOOOO0O000000O00 /O00OO00O00OOOO000 ))#line:3772
            else :#line:3773
                return O0000O0O000O00O00 .zoom (int (O00OO00O00OOOO000 /OOOOOO0O000000O00 ))#line:3774
        else :#line:3775
            OO0O0OOOO0OO0O00O =O0000O0O000O00O00 .width ()#line:3776
            O0OO0OO00000OOOO0 =O0000O0O000O00O00 .height ()#line:3777
            OOOOOO0O000000O00 =max (OO0O0OOOO0OO0O00O ,O0OO0OO00000OOOO0 )#line:3778
            O00OO00O00OOOO000 =max (OOO000O00O00OOOOO ,O0OO00OO0000OOOO0 )#line:3779
            if OOOOOO0O000000O00 >O00OO00O00OOOO000 :#line:3780
                return O0000O0O000O00O00 .subsample (OOOOOO0O000000O00 /O00OO00O00OOOO000 )#line:3781
            else :#line:3782
                return O0000O0O000O00O00 .zoom (O00OO00O00OOOO000 /OOOOOO0O000000O00 )#line:3783
    def forgot_callback (O0OO000O00O0O0OO0 ,O0O0O000OOOOO0OO0 ):#line:3785
        webbrowser .open ("https://www.snapeda.com/account/password_reset/",new =2 )#line:3786
    def register_callback (O0O0O0O0OO0OO00OO ,OOO0000OOOOOOO00O ):#line:3788
        webbrowser .open ("https://www.snapeda.com/account/signup/",new =2 )#line:3789
    def initialize_user_interface (OOO0OOO0O0O0O00OO ):#line:3792
        if OOO0OOO0O0O0O00OO .is_windows :#line:3793
            OOO0OOO0O0O0O00OO .parent .iconbitmap (OOO0OOO0O0O0O00OO .icon_bitmap_dir )#line:3794
        OOO0OOO0O0O0O00OO .parent .title ("SnapEDA v"+OOO0OOO0O0O0O00OO .parent .version )#line:3795
        OOO0OOO0O0O0O00OO .login_frame =tk .Frame (OOO0OOO0O0O0O00OO .parent ,bg ="white")#line:3796
        OOO0OOO0O0O0O00OO .login_frame .grid (row =0 ,column =0 ,sticky ="NEWS")#line:3797
        O0000000OO0OOOOO0 =tk .PhotoImage (file =os .path .join (OOO0OOO0O0O0O00OO .login_bg_image_dir ))#line:3799
        OOO0OOO0O0O0O00OO .login_bg_image =OOO0OOO0O0O0O00OO .resize (O0000000OO0OOOOO0 ,458 ,721 )#line:3800
        OOO0OOO0O0O0O00OO .login_bg =tk .Label (OOO0OOO0O0O0O00OO .login_frame ,image =OOO0OOO0O0O0O00OO .login_bg_image ,bg ="white")#line:3801
        OOO0OOO0O0O0O00OO .login_bg .grid (row =0 ,column =0 ,sticky ="NEWS",rowspan =6 ,columnspan =2 )#line:3802
        for O0O0O00000000OO0O in range (6 ):#line:3803
            if O0O0O00000000OO0O <2 :#line:3804
                OOO0OOO0O0O0O00OO .login_frame .grid_columnconfigure (O0O0O00000000OO0O ,weight =1 ,uniform ="foo")#line:3805
            OOO0OOO0O0O0O00OO .login_frame .grid_rowconfigure (O0O0O00000000OO0O ,weight =1 )#line:3806
        OOO0OOO0O0O0O00OO .label =tk .Label (OOO0OOO0O0O0O00OO .login_frame ,text ="",bg ="white")#line:3819
        OOO0OOO0O0O0O00OO .label .grid (row =0 ,column =0 ,columnspan =2 ,sticky ="S",pady =(250 ,0 ))#line:3820
        OOO0OOO0O0O0O00OO .userpass_frame =tk .Frame (OOO0OOO0O0O0O00OO .login_frame ,bg ="white")#line:3822
        OOO0OOO0O0O0O00OO .userpass_frame .grid (row =1 ,column =0 ,columnspan =2 )#line:3823
        O0O0000OOO000OO0O =tk .PhotoImage (file =os .path .join (OOO0OOO0O0O0O00OO .username_bg_image_dir ))#line:3825
        OOO0OOO0O0O0O00OO .username_bg_image =OOO0OOO0O0O0O00OO .resize (O0O0000OOO000OO0O ,229 ,34 )#line:3826
        OOO0OOO0O0O0O00OO .username_image =tk .Label (OOO0OOO0O0O0O00OO .userpass_frame ,image =OOO0OOO0O0O0O00OO .username_bg_image ,bg ="white")#line:3827
        OOO0OOO0O0O0O00OO .username_image .grid (row =0 ,column =0 ,sticky ="W")#line:3828
        OOO0OOO0O0O0O00OO .username_entry =tk .Entry (OOO0OOO0O0O0O00OO .userpass_frame ,font =("Open Sans","10"),bg ="#C4C4C4",borderwidth =0 ,highlightthickness =0 )#line:3829
        OOO0OOO0O0O0O00OO .username_entry .insert (0 ,"Username or Email")#line:3830
        OOO0OOO0O0O0O00OO .username_entry .grid (row =0 ,column =0 ,padx =(5 ,0 ))#line:3831
        OOO0OOO0O0O0O00OO .username_entry .bind ('<FocusIn>',OOO0OOO0O0O0O00OO .on_entry_click_username )#line:3832
        OOO0OOO0O0O0O00OO .username_entry .bind ('<FocusOut>',OOO0OOO0O0O0O00OO .on_focusout_username )#line:3833
        OOO0OOO0O0O0O00OO .username_entry .config (fg ='black')#line:3834
        O000O0O0O00O0O0OO =tk .PhotoImage (file =os .path .join (OOO0OOO0O0O0O00OO .password_bg_image_dir ))#line:3837
        OOO0OOO0O0O0O00OO .password_bg_image =OOO0OOO0O0O0O00OO .resize (O000O0O0O00O0O0OO ,229 ,34 )#line:3838
        OOO0OOO0O0O0O00OO .password_image =tk .Label (OOO0OOO0O0O0O00OO .userpass_frame ,image =OOO0OOO0O0O0O00OO .password_bg_image ,bg ="white")#line:3839
        OOO0OOO0O0O0O00OO .password_image .grid (row =1 ,column =0 ,sticky ="W",pady =(20 ,0 ))#line:3840
        OOO0OOO0O0O0O00OO .password_entry =tk .Entry (OOO0OOO0O0O0O00OO .userpass_frame ,font =("Open Sans","10"),bg ="#C4C4C4",borderwidth =0 ,highlightthickness =0 )#line:3841
        OOO0OOO0O0O0O00OO .password_entry .insert (0 ,"Password")#line:3842
        OOO0OOO0O0O0O00OO .password_entry .grid (row =1 ,column =0 ,padx =(5 ,0 ),pady =(20 ,0 ))#line:3843
        OOO0OOO0O0O0O00OO .password_entry .bind ('<FocusIn>',OOO0OOO0O0O0O00OO .on_entry_click_password )#line:3844
        OOO0OOO0O0O0O00OO .password_entry .bind ('<FocusOut>',OOO0OOO0O0O0O00OO .on_focusout_password )#line:3845
        OOO0OOO0O0O0O00OO .password_entry .config (fg ='black')#line:3846
        OOO0OOO0O0O0O00OO .username_entry .bind ('<Return>',OOO0OOO0O0O0O00OO .check_login_thread )#line:3849
        OOO0OOO0O0O0O00OO .password_entry .bind ('<Return>',OOO0OOO0O0O0O00OO .check_login_thread )#line:3850
        OOO0OOO0O0O0O00OO .forgot_password =tk .Label (OOO0OOO0O0O0O00OO .userpass_frame ,text ="Forgot Password?",fg ="#696969",cursor ="hand2",bg ="white")#line:3853
        OOO0OOO0O0O0O00OO .forgot_password .grid (row =2 ,column =0 ,pady =(11 ,0 ))#line:3854
        OOO0OOO0O0O0O00OO .forgot_password .bind ("<Button-1>",OOO0OOO0O0O0O00OO .forgot_callback )#line:3855
        OOO0O0OOO0O00O000 =tk .PhotoImage (file =os .path .join (OOO0OOO0O0O0O00OO .login_button_image_dir ))#line:3858
        OOO0OOO0O0O0O00OO .login_button_image =OOO0OOO0O0O0O00OO .resize (OOO0O0OOO0O00O000 ,173 ,42 )#line:3859
        OOO0OOO0O0O0O00OO .login_button =tk .Label (OOO0OOO0O0O0O00OO .login_frame ,text ="",cursor ="hand2",bg ="white",image =OOO0OOO0O0O0O00OO .login_button_image )#line:3864
        OOO0OOO0O0O0O00OO .login_button .grid (row =2 ,column =0 ,columnspan =2 ,pady =(15 ,4 ))#line:3865
        OOO0OOO0O0O0O00OO .login_button .bind ("<Button-1>",OOO0OOO0O0O0O00OO .check_login_thread )#line:3866
        OOO0OOO0O0O0O00OO .register_frame =tk .Frame (OOO0OOO0O0O0O00OO .login_frame ,bg ="white")#line:3868
        OOO0OOO0O0O0O00OO .register_frame .grid (row =2 ,column =0 ,columnspan =2 ,sticky ="S")#line:3869
        O0OOOOOO00OOOOO00 =tk .Label (OOO0OOO0O0O0O00OO .register_frame ,bg ="white",fg ="#696969",text ="Don't have an account?",font =("Open Sans","8"))#line:3870
        O0OOOOOO00OOOOO00 .grid (row =0 ,column =0 ,sticky ="N")#line:3871
        OOO0OOO0O0O0O00OO .register_button =tk .Label (OOO0OOO0O0O0O00OO .register_frame ,text ="Register",fg ="#FF761B",cursor ="hand2",bg ="white",font =("Open Sans","8","bold"))#line:3881
        OOO0OOO0O0O0O00OO .register_button .grid (row =0 ,column =1 ,pady =(0 ,0 ),sticky ="N")#line:3882
        OOO0OOO0O0O0O00OO .register_button .bind ("<Button-1>",OOO0OOO0O0O0O00OO .register_callback )#line:3883
class InstallScreen (tk .Frame ):#line:3885
    ""#line:3891
    def __init__ (OOO000OO0O0OOOOOO ,O00O0OO0OO00O0O00 ):#line:3893
        tk .Frame .__init__ (OOO000OO0O0OOOOOO ,O00O0OO0OO00O0O00 )#line:3894
        OOO000OO0O0OOOOOO .parent =O00O0OO0OO00O0O00 #line:3895
        OOO000OO0O0OOOOOO .version =O00O0OO0OO00O0O00 .version #line:3896
        OOO000OO0O0OOOOOO .parent .geometry (CONST_INSTALL_WINDOW_GEOMETRY )#line:3897
        OOO000OO0O0OOOOOO .parent .minsize (width =CONST_INSTALL_WINDOW_WIDTH ,height =CONST_INSTALL_GEOMETRY_HEIGHT )#line:3898
        OOO000OO0O0OOOOOO .parent .grid_columnconfigure (0 ,weight =1 )#line:3899
        OOO000OO0O0OOOOOO .parent .grid_rowconfigure (0 ,weight =1 )#line:3900
        OOO000OO0O0OOOOOO .initialize_user_interface ()#line:3901
    def image_return (O0OO0O0OO00O00O0O ,OOOO0O0000000OO00 ):#line:3903
        return OOOO0O0000000OO00 #line:3904
    def download_ico (OO000OO00000OO0OO ,OO00OOO00OOO0000O ):#line:3906
        if sys .version_info [0 ]==3 :#line:3907
            urllib .request .urlretrieve (OO00OOO00OOO0000O ,OO000OO00000OO0OO .icon_bitmap_dir )#line:3908
        else :#line:3909
            urllib .urlretrieve (OO00OOO00OOO0000O ,OO000OO00000OO0OO .icon_bitmap_dir )#line:3910
    def download_image (OO000O0O00O0O0O0O ,O0O0O00O00O0OO000 ):#line:3912
        OO0000O0OO000O0O0 =O0O0O00O00O0OO000 [O0O0O00O00O0OO000 .rfind ('/')+1 :]#line:3913
        OO0O0OO0OO00OO0OO =os .path .join (OO000O0O00O0O0O0O .appdata_dir ,OO0000O0OO000O0O0 )#line:3914
        OO0O000OO000O00OO =OO0O0OO0OO00OO0OO [:-3 ]+"png"#line:3915
        OO0OO0OO0OO00OOOO =threading .Timer (2 ,OO000O0O00O0O0O0O .image_return ,args =(OO0O000OO000O00OO ,))#line:3916
        OO0OO0OO0OO00OOOO .start ()#line:3917
        if not os .path .exists (OO0O000OO000O00OO )and not OO000O0O00O0O0O0O .is_mac :#line:3918
            if OO000O0O00O0O0O0O .is_windows :#line:3919
                O0OOOO0OOO000000O =os .path .join (os .path .dirname (__file__ ),"imagemagick","convert")#line:3920
                subprocess .check_call ([O0OOOO0OOO000000O ,O0O0O00O00O0OO000 .replace ("https","http"),OO0O000OO000O00OO ],shell =True )#line:3921
            else :#line:3922
                subprocess .call ("convert "+O0O0O00O00O0OO000 .replace ("https","http")+" "+OO0O000OO000O00OO ,shell =True )#line:3923
        if OO000O0O00O0O0O0O .is_mac :#line:3924
            if not os .path .exists (OO0O000OO000O00OO ):#line:3925
                with open (OO0O0OO0OO00OO0OO ,"wb")as OO0O0OOO0O0OOOO0O :#line:3926
                    if sys .version_info [0 ]==3 :#line:3927
                        O0OO00O0O0O00OO00 =urllib .request .urlopen (O0O0O00O00O0OO000 ).read ()#line:3928
                    else :#line:3929
                        O0OO00O0O0O00OO00 =urllib2 .urlopen (O0O0O00O00O0OO000 ).read ()#line:3930
                    OO0O0OOO0O0OOOO0O .write (O0OO00O0O0O00OO00 )#line:3931
                    OO0O0OOO0O0OOOO0O .close ()#line:3932
                    subprocess .check_call (["sips","-s","format","gif","%s"%OO0O0OO0OO00OO0OO ,"--out","%s"%OO0O000OO000O00OO ],shell =True )#line:3933
        return OO0O000OO000O00OO #line:3934
    def setup_dirs (OOOOOOOO000O0OO0O ):#line:3936
        ""#line:3939
        OOOOOOOO000O0OO0O .dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:3940
        OOOOOOOO000O0OO0O .is_mac =platform .mac_ver ()[0 ]!=""#line:3941
        OOOOOOOO000O0OO0O .is_windows =(os .name =='nt')#line:3942
        if OOOOOOOO000O0OO0O .is_windows :#line:3943
            OOOOOOOO000O0OO0O .windata_dir =os .path .join (os .getenv ('HOMEDRIVE'),os .getenv ('HOMEPATH'),"SnapEDA Kicad Plugin")#line:3946
            OOOOOOOO000O0OO0O .appdata_dir =os .path .join (OOOOOOOO000O0OO0O .windata_dir ,"App")#line:3947
            OOOOOOOO000O0OO0O .flip_table_dir =os .path .join (os .getenv ('APPDATA'),'kicad','fp-lib-table')#line:3950
            OOOOOOOO000O0OO0O .kicad_common_dir =os .path .join (os .getenv ('APPDATA'),'kicad','kicad_common')#line:3953
            OOOOOOOO000O0OO0O .kicad_library_dir =os .path .join (OOOOOOOO000O0OO0O .windata_dir ,'KiCad Library')#line:3954
            OOOOOOOO000O0OO0O .snapeda_library_dir =os .path .join (OOOOOOOO000O0OO0O .kicad_library_dir ,'SnapEDA Library')#line:3957
            OOOOOOOO000O0OO0O .snapeda_library_abs_dir =os .path .join (OOOOOOOO000O0OO0O .kicad_library_dir ,'SnapEDA Library.pretty')#line:3959
            OOOOOOOO000O0OO0O .snapeda_threedee_models_dir =os .path .join (OOOOOOOO000O0OO0O .kicad_library_dir ,'SnapEDA 3D Models')#line:3961
            if not os .path .exists (OOOOOOOO000O0OO0O .windata_dir ):#line:3963
                os .makedirs (OOOOOOOO000O0OO0O .windata_dir )#line:3964
            if not os .path .exists (OOOOOOOO000O0OO0O .appdata_dir ):#line:3965
                os .makedirs (OOOOOOOO000O0OO0O .appdata_dir )#line:3966
            if not os .path .exists (OOOOOOOO000O0OO0O .kicad_library_dir ):#line:3967
                os .makedirs (OOOOOOOO000O0OO0O .kicad_library_dir )#line:3968
            if not os .path .exists (OOOOOOOO000O0OO0O .snapeda_library_dir ):#line:3969
                os .makedirs (OOOOOOOO000O0OO0O .snapeda_library_dir )#line:3970
            if not os .path .exists (OOOOOOOO000O0OO0O .snapeda_library_abs_dir ):#line:3971
                os .makedirs (OOOOOOOO000O0OO0O .snapeda_library_abs_dir )#line:3972
            if not os .path .exists (OOOOOOOO000O0OO0O .snapeda_threedee_models_dir ):#line:3973
                os .makedirs (OOOOOOOO000O0OO0O .snapeda_threedee_models_dir )#line:3974
        elif OOOOOOOO000O0OO0O .is_mac :#line:3975
            OOOOOOOO000O0OO0O .macdata_dir =os .path .join (os .path .expanduser ("~"),"Documents","SnapEDA Kicad Plugin")#line:3976
            OOOOOOOO000O0OO0O .appdata_dir =os .path .join (OOOOOOOO000O0OO0O .macdata_dir ,"App")#line:3977
            OOOOOOOO000O0OO0O .flip_table_dir =os .path .join (os .getenv ('HOME'),'library','preferences','kicad','fp-lib-table')#line:3978
            OOOOOOOO000O0OO0O .kicad_common_dir =os .path .join (os .getenv ('HOME'),'library','preferences','kicad','kicad_common')#line:3979
            OOOOOOOO000O0OO0O .kicad_library_dir =os .path .join (OOOOOOOO000O0OO0O .macdata_dir ,'KiCad Library')#line:3980
            OOOOOOOO000O0OO0O .snapeda_library_dir =os .path .join (OOOOOOOO000O0OO0O .kicad_library_dir ,'SnapEDA Library')#line:3982
            OOOOOOOO000O0OO0O .snapeda_library_abs_dir =os .path .join (OOOOOOOO000O0OO0O .kicad_library_dir ,'SnapEDA Library.pretty')#line:3984
            OOOOOOOO000O0OO0O .snapeda_threedee_models_dir =os .path .join (OOOOOOOO000O0OO0O .kicad_library_dir ,'SnapEDA 3D Models')#line:3986
            if not os .path .exists (OOOOOOOO000O0OO0O .appdata_dir ):#line:3988
                os .makedirs (OOOOOOOO000O0OO0O .appdata_dir )#line:3989
            if not os .path .exists (OOOOOOOO000O0OO0O .kicad_library_dir ):#line:3990
                os .makedirs (OOOOOOOO000O0OO0O .kicad_library_dir )#line:3991
            if not os .path .exists (OOOOOOOO000O0OO0O .snapeda_library_dir ):#line:3992
                os .makedirs (OOOOOOOO000O0OO0O .snapeda_library_dir )#line:3993
            if not os .path .exists (OOOOOOOO000O0OO0O .snapeda_library_abs_dir ):#line:3994
                os .makedirs (OOOOOOOO000O0OO0O .snapeda_library_abs_dir )#line:3995
            if not os .path .exists (OOOOOOOO000O0OO0O .snapeda_threedee_models_dir ):#line:3996
                os .makedirs (OOOOOOOO000O0OO0O .snapeda_threedee_models_dir )#line:3997
        else :#line:3998
            OOOOOOOO000O0OO0O .appdata_dir =os .path .join (OOOOOOOO000O0OO0O .dir_path ,"assets")#line:3999
            OOOOOOOO000O0OO0O .flip_table_dir =os .path .join (os .path .expanduser ("~"),'.config','kicad','fp-lib-table')#line:4003
            OOOOOOOO000O0OO0O .kicad_common_dir =os .path .join (os .path .expanduser ("~"),'.config','kicad','kicad_common')#line:4007
            O0000O0O000OOO0OO =os .path .expanduser ("~")#line:4008
            OOOOOOOO000O0OO0O .kicad_library_dir =os .path .join (O0000O0O000OOO0OO ,'KiCad Library')#line:4009
            OOOOOOOO000O0OO0O .snapeda_library_dir =os .path .join (OOOOOOOO000O0OO0O .kicad_library_dir ,'SnapEDA Library')#line:4011
            OOOOOOOO000O0OO0O .snapeda_library_abs_dir =os .path .join (OOOOOOOO000O0OO0O .kicad_library_dir ,'SnapEDA Library.pretty')#line:4013
            OOOOOOOO000O0OO0O .snapeda_threedee_models_dir =os .path .join (OOOOOOOO000O0OO0O .kicad_library_dir ,'SnapEDA 3D Models')#line:4015
            if not os .path .exists (OOOOOOOO000O0OO0O .appdata_dir ):#line:4016
                os .makedirs (OOOOOOOO000O0OO0O .appdata_dir )#line:4017
            if not os .path .exists (OOOOOOOO000O0OO0O .kicad_library_dir ):#line:4018
                os .makedirs (OOOOOOOO000O0OO0O .kicad_library_dir )#line:4019
            if not os .path .exists (OOOOOOOO000O0OO0O .snapeda_library_dir ):#line:4020
                os .makedirs (OOOOOOOO000O0OO0O .snapeda_library_dir )#line:4021
            if not os .path .exists (OOOOOOOO000O0OO0O .snapeda_library_abs_dir ):#line:4022
                os .makedirs (OOOOOOOO000O0OO0O .snapeda_library_abs_dir )#line:4023
            if not os .path .exists (OOOOOOOO000O0OO0O .snapeda_threedee_models_dir ):#line:4024
                os .makedirs (OOOOOOOO000O0OO0O .snapeda_threedee_models_dir )#line:4025
        OOO000OO00OO0O0OO =os .path .join (OOOOOOOO000O0OO0O .appdata_dir ,"info.json")#line:4028
        try :#line:4029
            with open (OOO000OO00OO0O0OO )as OOOOOOOO0O0O00OO0 :#line:4030
                OOOOOO0O0O0O000O0 =json .load (OOOOOOOO0O0O00OO0 )#line:4031
            if not OOOOOO0O0O0O000O0 ['version']==OOOOOOOO000O0OO0O .version :#line:4032
                OOOOOO0O0O0O000O0 ['version']=OOOOOOOO000O0OO0O .version #line:4033
                OOOOOO0O0O0O000O0 ['kicad_library_dir']=OOOOOOOO000O0OO0O .kicad_library_dir #line:4034
                OOOOOO0O0O0O000O0 ['kicad_library_name']='SnapEDA Library'#line:4035
                with open (OOO000OO00OO0O0OO ,'w')as O00OOO0OOO0O000OO :#line:4036
                    json .dump (OOOOOO0O0O0O000O0 ,O00OOO0OOO0O000OO )#line:4037
                print ('Replacing new version...')#line:4038
                OOOOOOOO000O0OO0O .is_installing =True #line:4039
        except :#line:4040
            OOOOOO0O0O0O000O0 ={}#line:4041
            OOOOOO0O0O0O000O0 ['version']=OOOOOOOO000O0OO0O .version #line:4042
            OOOOOO0O0O0O000O0 ['kicad_library_dir']=OOOOOOOO000O0OO0O .kicad_library_dir #line:4043
            OOOOOO0O0O0O000O0 ['kicad_library_name']='SnapEDA Library'#line:4044
            with open (OOO000OO00OO0O0OO ,'w')as O00OOO0OOO0O000OO :#line:4045
                json .dump (OOOOOO0O0O0O000O0 ,O00OOO0OOO0O000OO )#line:4046
            print ('Installing new version...')#line:4047
            OOOOOOOO000O0OO0O .is_installing =True #line:4048
        with open (OOOOOOOO000O0OO0O .kicad_common_dir ,"r+")as OOO0OOO00O000O00O :#line:4052
            O0OOO0O0OOO0OOO0O =OOO0OOO00O000O00O .read ()#line:4053
            if ("SNAPEDA_3D_MOD="+OOOOOOOO000O0OO0O .snapeda_threedee_models_dir )not in O0OOO0O0OOO0OOO0O :#line:4054
                OOOO00OO0O000OOOO ='\nSNAPEDA_3D_MOD='+OOOOOOOO000O0OO0O .snapeda_threedee_models_dir +'\n'#line:4055
                OOOO00OO0O000OOOO =OOOO00OO0O000OOOO .replace ("'","")#line:4056
                OO00O0OO00O000000 =O0OOO0O0OOO0OOO0O [:-2 ]+OOOO00OO0O000OOOO #line:4057
                OOO0OOO00O000O00O .seek (0 )#line:4058
                OOO0OOO00O000O00O .write (OO00O0OO00O000000 )#line:4059
                OOO0OOO00O000O00O .truncate ()#line:4060
    def continue_installation_callback (O00OO0000OOOO0O0O ,O0OOOO0O0OO00OO00 ):#line:4084
        for O0OO00OO0OO000OOO in O00OO0000OOOO0O0O .parent .grid_slaves ():#line:4085
            O0OO00OO0OO000OOO .destroy ()#line:4086
        LoginScreen (O00OO0000OOOO0O0O .parent )#line:4087
    def installation_process (OO0OOO0OO0O00O0O0 ):#line:4089
        try :#line:4091
            if OO0OOO0OO0O00O0O0 .is_windows or OO0OOO0OO0O00O0O0 .is_mac :#line:4092
                os .remove (os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'.token'))#line:4093
            else :#line:4094
                os .remove (os .path .join (OO0OOO0OO0O00O0O0 .dir_path ,".token"))#line:4095
        except :#line:4096
            pass #line:4097
        OO0OOO0OO0O00O0O0 .login_bg_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"Group+292.png")#line:4099
        OO0OOO0OO0O00O0O0 .username_bg_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"3xm843ff.png")#line:4100
        OO0OOO0OO0O00O0O0 .password_bg_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"ek8owdjt.png")#line:4101
        OO0OOO0OO0O00O0O0 .login_button_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"g4pik2y2.png")#line:4102
        OO0OOO0OO0O00O0O0 .logo_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"lkeixquo.png")#line:4103
        OO0OOO0OO0O00O0O0 .loading_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"jwhk6qck.gif")#line:4104
        OO0OOO0OO0O00O0O0 .cover_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"RefDesign.png")#line:4105
        OO0OOO0OO0O00O0O0 .symbol_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"Symbol.png")#line:4106
        OO0OOO0OO0O00O0O0 .package_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"Footprint.png")#line:4108
        if not os .path .exists (OO0OOO0OO0O00O0O0 .logo_image_dir ):#line:4109
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/lkeixquo.png")#line:4110
        if not os .path .exists (OO0OOO0OO0O00O0O0 .loading_image_dir ):#line:4112
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/jwhk6qck.gif")#line:4113
        if not os .path .exists (OO0OOO0OO0O00O0O0 .cover_image_dir ):#line:4114
            OO0OOO0OO0O00O0O0 .download_image ("https://s3.amazonaws.com/snapeda/ulp/RefDesign.png")#line:4116
        if not os .path .exists (OO0OOO0OO0O00O0O0 .symbol_image_dir ):#line:4117
            OO0OOO0OO0O00O0O0 .download_image ("https://s3.amazonaws.com/snapeda/ulp/Symbol.png")#line:4119
        if not os .path .exists (OO0OOO0OO0O00O0O0 .package_image_dir ):#line:4120
            OO0OOO0OO0O00O0O0 .download_image ("https://s3.amazonaws.com/snapeda/ulp/Footprint.png")#line:4122
        if not os .path .exists (OO0OOO0OO0O00O0O0 .login_bg_image_dir ):#line:4123
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/Group+292.png")#line:4125
        if not os .path .exists (OO0OOO0OO0O00O0O0 .username_bg_image_dir ):#line:4126
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/3xm843ff.png")#line:4128
        if not os .path .exists (OO0OOO0OO0O00O0O0 .password_bg_image_dir ):#line:4129
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/ek8owdjt.png")#line:4131
        if not os .path .exists (OO0OOO0OO0O00O0O0 .login_button_image_dir ):#line:4132
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/g4pik2y2.png")#line:4134
        OO0OOO0OO0O00O0O0 .welcome_screen_001_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"Mask+Group.png")#line:4137
        OO0OOO0OO0O00O0O0 .welcome_screen_002_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"icon1.bbe45f7648f7.png")#line:4138
        OO0OOO0OO0O00O0O0 .welcome_screen_003_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"ico_deadlines.8ba69c3f942a.png")#line:4139
        OO0OOO0OO0O00O0O0 .welcome_screen_004_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"icon2.924b03ebfccc.png")#line:4140
        OO0OOO0OO0O00O0O0 .welcome_screen_005_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"powered+by+snapEDA.png")#line:4141
        OO0OOO0OO0O00O0O0 .welcome_screen_006_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"snapeda-transparent.png")#line:4142
        OO0OOO0OO0O00O0O0 .usb_type_c_button_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"usb+type+c.png")#line:4143
        OO0OOO0OO0O00O0O0 .microcontroller_button_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"usb+microcontroller.png")#line:4144
        if not os .path .exists (OO0OOO0OO0O00O0O0 .welcome_screen_001_dir ):#line:4146
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Designs+-+API/Mask+Group.png")#line:4148
        if not os .path .exists (OO0OOO0OO0O00O0O0 .welcome_screen_002_dir ):#line:4149
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/icon1.bbe45f7648f7.png")#line:4151
        if not os .path .exists (OO0OOO0OO0O00O0O0 .welcome_screen_003_dir ):#line:4152
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/ico_deadlines.8ba69c3f942a.png")#line:4154
        if not os .path .exists (OO0OOO0OO0O00O0O0 .welcome_screen_004_dir ):#line:4155
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/icon2.924b03ebfccc.png")#line:4157
        if not os .path .exists (OO0OOO0OO0O00O0O0 .welcome_screen_005_dir ):#line:4158
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Designs+-+API/powered+by+snapEDA.png")#line:4160
        if not os .path .exists (OO0OOO0OO0O00O0O0 .welcome_screen_006_dir ):#line:4161
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/snapeda-transparent.png")#line:4163
        if not os .path .exists (OO0OOO0OO0O00O0O0 .usb_type_c_button_dir ):#line:4164
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/usb+type+c.png")#line:4166
        if not os .path .exists (OO0OOO0OO0O00O0O0 .microcontroller_button_dir ):#line:4167
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/usb+microcontroller.png")#line:4169
        OO0OOO0OO0O00O0O0 .filter_button_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"neeo2s8g.png")#line:4171
        OO0OOO0OO0O00O0O0 .settings_button_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"7svfoe57.png")#line:4172
        OO0OOO0OO0O00O0O0 .about_button_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"2kdtezsl.png")#line:4173
        OO0OOO0OO0O00O0O0 .passive_components_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"t3gwhnzh.png")#line:4174
        OO0OOO0OO0O00O0O0 .all_button_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"dsyrvfl9.png")#line:4175
        OO0OOO0OO0O00O0O0 .powered_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"orb6glbv.png")#line:4176
        OO0OOO0OO0O00O0O0 .datasheet_button_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"oxfarxz8.png")#line:4177
        OO0OOO0OO0O00O0O0 .datasheet_available_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"m4lamm2w.png")#line:4178
        OO0OOO0OO0O00O0O0 .datasheet_not_available_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"4cnn9kkf.png")#line:4179
        OO0OOO0OO0O00O0O0 .symbol_available_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"huaxvbtm.png")#line:4180
        OO0OOO0OO0O00O0O0 .symbol_not_available_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"tmuhgmxh.png")#line:4181
        OO0OOO0OO0O00O0O0 .footprint_available_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"3ruuehki.png")#line:4182
        OO0OOO0OO0O00O0O0 .footprint_not_available_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"footprint_outline.cebd715affd8.png")#line:4183
        OO0OOO0OO0O00O0O0 .available_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"uku4ceuv.png")#line:4184
        OO0OOO0OO0O00O0O0 .not_available_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"zah3n8r4.png")#line:4185
        OO0OOO0OO0O00O0O0 .prev_bg_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"iu2ma3jp.png")#line:4186
        OO0OOO0OO0O00O0O0 .next_bg_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"witafnjf.png")#line:4187
        OO0OOO0OO0O00O0O0 .selected_page_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"izif2qd8.png")#line:4188
        OO0OOO0OO0O00O0O0 .download_button_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"download+orange.png")#line:4189
        OO0OOO0OO0O00O0O0 .view_button_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"viewonsnapeda+white.png")#line:4190
        OO0OOO0OO0O00O0O0 .search_button_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"4i2efbui.png")#line:4191
        OO0OOO0OO0O00O0O0 .loading_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"jwhk6qck.gif")#line:4192
        OO0OOO0OO0O00O0O0 .icon_bitmap_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"32x32.ico")#line:4193
        if not os .path .exists (OO0OOO0OO0O00O0O0 .filter_button_image_dir ):#line:4194
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/neeo2s8g.png")#line:4195
        if not os .path .exists (OO0OOO0OO0O00O0O0 .settings_button_image_dir ):#line:4196
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/7svfoe57.png")#line:4197
        if not os .path .exists (OO0OOO0OO0O00O0O0 .about_button_image_dir ):#line:4198
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/2kdtezsl.png")#line:4199
        if not os .path .exists (OO0OOO0OO0O00O0O0 .passive_components_image_dir ):#line:4200
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/t3gwhnzh.png")#line:4201
        if not os .path .exists (OO0OOO0OO0O00O0O0 .all_button_image_dir ):#line:4202
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/dsyrvfl9.png")#line:4203
        if not os .path .exists (OO0OOO0OO0O00O0O0 .powered_image_dir ):#line:4204
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/orb6glbv.png")#line:4205
        if not os .path .exists (OO0OOO0OO0O00O0O0 .datasheet_button_dir ):#line:4206
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/oxfarxz8.png")#line:4207
        if not os .path .exists (OO0OOO0OO0O00O0O0 .datasheet_available_dir ):#line:4208
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/m4lamm2w.png")#line:4209
        if not os .path .exists (OO0OOO0OO0O00O0O0 .datasheet_not_available_dir ):#line:4210
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/4cnn9kkf.png")#line:4211
        if not os .path .exists (OO0OOO0OO0O00O0O0 .symbol_available_dir ):#line:4212
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/huaxvbtm.png")#line:4213
        if not os .path .exists (OO0OOO0OO0O00O0O0 .symbol_not_available_dir ):#line:4214
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/tmuhgmxh.png")#line:4215
        if not os .path .exists (OO0OOO0OO0O00O0O0 .footprint_available_dir ):#line:4216
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/3ruuehki.png")#line:4217
        if not os .path .exists (OO0OOO0OO0O00O0O0 .footprint_not_available_dir ):#line:4218
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/62r7iuz7.png")#line:4219
        if not os .path .exists (OO0OOO0OO0O00O0O0 .available_dir ):#line:4220
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/uku4ceuv.png")#line:4221
        if not os .path .exists (OO0OOO0OO0O00O0O0 .not_available_dir ):#line:4222
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/zah3n8r4.png")#line:4223
        if not os .path .exists (OO0OOO0OO0O00O0O0 .prev_bg_dir ):#line:4224
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/iu2ma3jp.png")#line:4225
        if not os .path .exists (OO0OOO0OO0O00O0O0 .next_bg_dir ):#line:4226
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/witafnjf.png")#line:4227
        if not os .path .exists (OO0OOO0OO0O00O0O0 .selected_page_dir ):#line:4228
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/izif2qd8.png")#line:4229
        if not os .path .exists (OO0OOO0OO0O00O0O0 .download_button_dir ):#line:4230
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/download+orange.png")#line:4231
        if not os .path .exists (OO0OOO0OO0O00O0O0 .view_button_dir ):#line:4232
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/viewonsnapeda+white.png")#line:4233
        if not os .path .exists (OO0OOO0OO0O00O0O0 .search_button_image_dir ):#line:4234
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/4i2efbui.png")#line:4235
        if not os .path .exists (OO0OOO0OO0O00O0O0 .icon_bitmap_dir ):#line:4236
            OO0OOO0OO0O00O0O0 .download_ico ("https://snapeda.s3.amazonaws.com/Kicadplugin/32x32.ico")#line:4237
        OO0OOO0OO0O00O0O0 .avatar_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"avatar1.png")#line:4239
        if not os .path .exists (OO0OOO0OO0O00O0O0 .avatar_image_dir ):#line:4240
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/avatar1.png")#line:4241
        OO0OOO0OO0O00O0O0 .home_menu_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'home_menu.png')#line:4243
        OO0OOO0OO0O00O0O0 .how_it_works_menu_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'how_it_works_menu.png')#line:4244
        OO0OOO0OO0O00O0O0 .info_menu_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'info_menu.png')#line:4245
        OO0OOO0OO0O00O0O0 .logout_menu_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'logout_menu.png')#line:4246
        OO0OOO0OO0O00O0O0 .settings_menu_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'settings_menu.png')#line:4247
        OO0OOO0OO0O00O0O0 .update_menu_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'update_menu.png')#line:4248
        OO0OOO0OO0O00O0O0 .info_label_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'info_button.png')#line:4249
        OO0OOO0OO0O00O0O0 .info_placeholder_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'info_placeholder.png')#line:4250
        OO0OOO0OO0O00O0O0 .ok_button_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'ok_button.png')#line:4251
        OO0OOO0OO0O00O0O0 .setting_placeholder_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'settings_placeholder.png')#line:4252
        OO0OOO0OO0O00O0O0 .settings_input_placeholder_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'settings_input_placeholder.png')#line:4253
        OO0OOO0OO0O00O0O0 .settings_label_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'settings_button.png')#line:4254
        OO0OOO0OO0O00O0O0 .save_button_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'save_button.png')#line:4255
        OO0OOO0OO0O00O0O0 .folder_label_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'folder_label.png')#line:4256
        OO0OOO0OO0O00O0O0 .not_available_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'not_available.png')#line:4257
        OO0OOO0OO0O00O0O0 .request_now_button_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'request_now_button.png')#line:4258
        OO0OOO0OO0O00O0O0 .talk_to_us_button_image_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'talk_to_us_button.png')#line:4259
        OO0OOO0OO0O00O0O0 .update_notif_button_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,'notif_update_menu+(2).png')#line:4260
        OO0OOO0OO0O00O0O0 .threedee_model_not_available_img_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"3d_model_not_available_img.png")#line:4261
        if not os .path .exists (OO0OOO0OO0O00O0O0 .talk_to_us_button_image_dir ):#line:4263
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/talk_to_us_button.png")#line:4264
        if not os .path .exists (OO0OOO0OO0O00O0O0 .update_menu_img_dir ):#line:4265
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/update_menu.png")#line:4266
        if not os .path .exists (OO0OOO0OO0O00O0O0 .setting_placeholder_img_dir ):#line:4267
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/settings_placeholder.png")#line:4268
        if not os .path .exists (OO0OOO0OO0O00O0O0 .how_it_works_menu_img_dir ):#line:4269
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/how_it_works_menu.png")#line:4270
        if not os .path .exists (OO0OOO0OO0O00O0O0 .home_menu_img_dir ):#line:4271
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/home_menu.png")#line:4272
        if not os .path .exists (OO0OOO0OO0O00O0O0 .settings_menu_img_dir ):#line:4273
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/settings_menu.png")#line:4274
        if not os .path .exists (OO0OOO0OO0O00O0O0 .settings_input_placeholder_dir ):#line:4275
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/settings_input_placeholder.png")#line:4276
        if not os .path .exists (OO0OOO0OO0O00O0O0 .settings_label_img_dir ):#line:4277
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/settings_button.png")#line:4278
        if not os .path .exists (OO0OOO0OO0O00O0O0 .save_button_img_dir ):#line:4279
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/save_button.png")#line:4280
        if not os .path .exists (OO0OOO0OO0O00O0O0 .ok_button_img_dir ):#line:4281
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/ok_button.png")#line:4282
        if not os .path .exists (OO0OOO0OO0O00O0O0 .logout_menu_img_dir ):#line:4283
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/logout_menu.png")#line:4284
        if not os .path .exists (OO0OOO0OO0O00O0O0 .info_placeholder_img_dir ):#line:4285
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/info_placeholder.png")#line:4286
        if not os .path .exists (OO0OOO0OO0O00O0O0 .info_menu_img_dir ):#line:4287
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/info_menu.png")#line:4288
        if not os .path .exists (OO0OOO0OO0O00O0O0 .info_label_img_dir ):#line:4289
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/info_button.png")#line:4290
        if not os .path .exists (OO0OOO0OO0O00O0O0 .folder_label_img_dir ):#line:4291
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/folder_label.png")#line:4292
        if not os .path .exists (OO0OOO0OO0O00O0O0 .not_available_img_dir ):#line:4293
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/not_available.png")#line:4294
        if not os .path .exists (OO0OOO0OO0O00O0O0 .request_now_button_img_dir ):#line:4295
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/request_now_button.png")#line:4296
        if not os .path .exists (OO0OOO0OO0O00O0O0 .update_notif_button_img_dir ):#line:4297
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/notif_update_menu+(2).png")#line:4298
        if not os .path .exists (OO0OOO0OO0O00O0O0 .threedee_model_not_available_img_dir ):#line:4299
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/3d_model_not_available_img.png")#line:4300
        OO0OOO0OO0O00O0O0 .threedee_available_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"threedee_model_available.png")#line:4302
        OO0OOO0OO0O00O0O0 .threedee_unavailable_dir =os .path .join (OO0OOO0OO0O00O0O0 .appdata_dir ,"threedee_model_unavailable.png")#line:4303
        if not os .path .exists (OO0OOO0OO0O00O0O0 .threedee_available_dir ):#line:4304
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/threedee_model_available.png")#line:4305
        if not os .path .exists (OO0OOO0OO0O00O0O0 .threedee_unavailable_dir ):#line:4306
            OO0OOO0OO0O00O0O0 .download_image ("https://snapeda.s3.amazonaws.com/Kicadplugin/threedee_model_unavailable.png")#line:4307
        OO0OOO0OO0O00O0O0 .instruction_header_label .set ("INSTALLATION COMPLETE")#line:4332
        OO0OOO0OO0O00O0O0 .install_frame .config (cursor ="hand2")#line:4333
        OO0OOO0OO0O00O0O0 .instruction_label .set ("Click screen to complete installation.\n Directing to login in screen in ")#line:4334
        OO0OOO0OO0O00O0O0 .install_frame .bind ("<Button-1>",OO0OOO0OO0O00O0O0 .continue_installation_callback )#line:4335
        for OOOO000O0O00OOOOO in range (5 ,0 ,-1 ):#line:4337
            tk .Label (OO0OOO0OO0O00O0O0 .install_frame ,text =OOOO000O0O00OOOOO ,fg ="white",bg ="#ff761a",font =("Open Sans","20","bold")).grid (row =2 ,column =0 ,sticky ="SEW")#line:4338
            time .sleep (1 )#line:4339
        for O0OO0O0000000OO00 in OO0OOO0OO0O00O0O0 .parent .grid_slaves ():#line:4341
            O0OO0O0000000OO00 .destroy ()#line:4342
        LoginScreen (OO0OOO0OO0O00O0O0 .parent )#line:4343
    def initialize_user_interface (O0000000OO0OO0O00 ):#line:4345
        O0000000OO0OO0O00 .is_installing =False #line:4346
        O0000000OO0OO0O00 .setup_dirs ()#line:4347
        if O0000000OO0OO0O00 .is_installing :#line:4349
            O0000000OO0OO0O00 .parent .title ("SnapEDA v"+O0000000OO0OO0O00 .parent .version )#line:4350
            O0000000OO0OO0O00 .parent .geometry (CONST_INSTALL_WINDOW_GEOMETRY )#line:4351
            O0000000OO0OO0O00 .parent .minsize (width =CONST_INSTALL_WINDOW_WIDTH ,height =CONST_INSTALL_GEOMETRY_HEIGHT )#line:4352
            OOO0O000OOOO000OO ="#ff761a"#line:4353
            O0000000OO0OO0O00 .install_frame =tk .Frame (O0000000OO0OO0O00 .parent ,bg =OOO0O000OOOO000OO )#line:4354
            for O00000O0000O00O00 in range (6 ):#line:4355
                O0000000OO0OO0O00 .install_frame .grid_rowconfigure (O00000O0000O00O00 ,weight =1 ,uniform ="foo")#line:4356
            O0000000OO0OO0O00 .install_frame .grid_columnconfigure (0 ,weight =1 )#line:4357
            O0000000OO0OO0O00 .install_frame .grid (row =0 ,column =0 ,sticky ="NEWS")#line:4358
            O0000000OO0OO0O00 .instruction_label =tk .StringVar ()#line:4359
            O0000000OO0OO0O00 .instruction_label .set ("Installation is starting.\nPlease wait for the installation to complete.")#line:4360
            O0000000OO0OO0O00 .instruction_header_label =tk .StringVar ()#line:4361
            O0000000OO0OO0O00 .instruction_header_label .set ("INSTALLING...")#line:4362
            O0000000OO0OO0O00 .install_title_label =tk .Label (O0000000OO0OO0O00 .install_frame ,textvariable =O0000000OO0OO0O00 .instruction_header_label ,fg ="white",bg =OOO0O000OOOO000OO ,font =("Open Sans","18","bold"))#line:4363
            O0000000OO0OO0O00 .install_title_label .grid (row =1 ,column =0 ,sticky ="SEW")#line:4364
            O0000000OO0OO0O00 .install_instructions_label =tk .Label (O0000000OO0OO0O00 .install_frame ,textvariable =O0000000OO0OO0O00 .instruction_label ,fg ="white",bg =OOO0O000OOOO000OO ,justify =tk .CENTER ,font =("Open Sans","13"))#line:4365
            O0000000OO0OO0O00 .install_instructions_label .grid (row =2 ,column =0 ,sticky ="NEW")#line:4366
            OOO0000O0OO0OOOOO =threading .Thread (target =O0000000OO0OO0O00 .installation_process )#line:4368
            OOO0000O0OO0OOOOO .start ()#line:4369
        else :#line:4370
            LoginScreen (O0000000OO0OO0O00 .parent )#line:4371
def boot_plugin ():#line:4373
    O0OOO0O00O0OOO00O =tk .Tk ()#line:4374
    O0OOO0O00O0OOO00O .geometry (CONST_DEFAULT_GEOMETRY )#line:4375
    O0OOO0O00O0OOO00O .minsize (width =CONST_DEFAULT_WINDOW_WIDTH ,height =CONST_DEFAULT_GEOMETRY_HEIGHT )#line:4376
    O0OOO0O00O0OOO00O .version =version #line:4377
    InstallScreen (O0OOO0O00O0OOO00O )#line:4378
    tk .mainloop ()#line:4379
for_production =True #line:4381
version ='0.0.6.0'#line:4382
ssl ._create_default_https_context =ssl ._create_unverified_context #line:4383
try :#line:4385
    if sys .version_info [0 ]==3 :#line:4386
        request =urllib .request .urlopen ("https://snapeda.s3.amazonaws.com/Kicadplugin/kicad_snapeda_plugin.json")#line:4387
    else :#line:4388
        try :#line:4389
            request =urllib2 .urlopen ("https://snapeda.s3.amazonaws.com/Kicadplugin/kicad_snapeda_plugin.json")#line:4390
        except :#line:4391
            request =urllib2 .urlopen ("https://snapeda.s3.amazonaws.com/Kicadplugin/kicad_snapeda_plugin.json")#line:4392
    data =json .load (request )#line:4393
    print (data )#line:4394
    release_version =data ['current_version_release']#line:4395
    if version >=release_version :#line:4396
        IS_UPDATED =True #line:4397
    try :#line:4399
        if sys .argv [1 ]=='standalone':#line:4400
            for_production =False #line:4401
    except :#line:4402
        pass #line:4403
except :#line:4404
    pass #line:4405
if for_production :#line:4407
    import pcbnew #line:4408
    import wx #line:4409
    class SnapEDAPlugin (pcbnew .ActionPlugin ):#line:4411
        def defaults (O0OOO00000O0O0OOO ):#line:4412
            O0OOO00000O0O0OOO .name ="SnapEDA"#line:4413
            O0OOO00000O0O0OOO .category ="SnapEDA Plugin"#line:4414
            O0OOO00000O0O0OOO .description ="Design faster with SnapEDA. Download CAD models for millions of electronic components, including schematic symbols, PCB footprints, and 3D models."#line:4415
            O0OOO00000O0O0OOO .show_toolbar_button =False #line:4416
        def Run (O000OO0O00O0O0000 ):#line:4418
            O0OOOO000O0O0O0O0 =threading .Thread (target =boot_plugin )#line:4421
            O0OOOO000O0O0O0O0 .setDaemon (True )#line:4422
            O0OOOO000O0O0O0O0 .start ()#line:4423
    SnapEDAPlugin ().register ()#line:4425
else :#line:4426
    boot_plugin ()