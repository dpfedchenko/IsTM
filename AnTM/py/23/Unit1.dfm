object Form1: TForm1
  Left = 525
  Top = 165
  Width = 1327
  Height = 729
  Caption = 'Form1'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Image1: TImage
    Left = 32
    Top = 16
    Width = 800
    Height = 200
  end
  object Label1: TLabel
    Left = 880
    Top = 80
    Width = 14
    Height = 13
    Caption = 'Nv'
  end
  object Label2: TLabel
    Left = 840
    Top = 112
    Width = 14
    Height = 13
    Caption = 'No'
  end
  object Label3: TLabel
    Left = 920
    Top = 112
    Width = 14
    Height = 13
    Caption = 'Ne'
  end
  object Label4: TLabel
    Left = 1160
    Top = 144
    Width = 46
    Height = 13
    Caption = 'epsilon_E'
  end
  object Label5: TLabel
    Left = 1160
    Top = 96
    Width = 45
    Height = 13
    Caption = 'epsilon_o'
  end
  object Label6: TLabel
    Left = 1000
    Top = 112
    Width = 12
    Height = 13
    Caption = 'Lo'
  end
  object Label7: TLabel
    Left = 1080
    Top = 112
    Width = 6
    Height = 13
    Caption = 'L'
  end
  object Label8: TLabel
    Left = 840
    Top = 200
    Width = 14
    Height = 13
    Caption = 'No'
  end
  object Label9: TLabel
    Left = 920
    Top = 200
    Width = 14
    Height = 13
    Caption = 'Ne'
  end
  object Label10: TLabel
    Left = 1000
    Top = 200
    Width = 12
    Height = 13
    Caption = 'Lo'
  end
  object Label11: TLabel
    Left = 1080
    Top = 200
    Width = 12
    Height = 13
    Caption = 'L2'
  end
  object Label12: TLabel
    Left = 840
    Top = 152
    Width = 14
    Height = 13
    Caption = 'Nd'
  end
  object Label13: TLabel
    Left = 920
    Top = 152
    Width = 12
    Height = 13
    Caption = 'Ld'
  end
  object Label14: TLabel
    Left = 1000
    Top = 152
    Width = 12
    Height = 13
    Caption = 'Fd'
  end
  object Label15: TLabel
    Left = 968
    Top = 624
    Width = 22
    Height = 13
    Caption = 'D_D'
  end
  object Label16: TLabel
    Left = 1176
    Top = 120
    Width = 26
    Height = 13
    Caption = 'mu_o'
  end
  object Label17: TLabel
    Left = 1176
    Top = 160
    Width = 27
    Height = 13
    Caption = 'mu_E'
  end
  object Image2: TImage
    Left = 56
    Top = 296
    Width = 800
    Height = 177
  end
  object Label18: TLabel
    Left = 856
    Top = 656
    Width = 27
    Height = 14
    Caption = 'Theta'
    Font.Charset = GREEK_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'MS Sans Serif'
    Font.Style = []
    ParentFont = False
  end
  object Label19: TLabel
    Left = 912
    Top = 656
    Width = 26
    Height = 13
    Caption = 'Phi_y'
  end
  object BitBtn1: TBitBtn
    Left = 848
    Top = 16
    Width = 137
    Height = 41
    Caption = 'Start'
    TabOrder = 0
    OnClick = BitBtn1Click
  end
  object Edit1: TEdit
    Left = 904
    Top = 80
    Width = 81
    Height = 21
    TabOrder = 1
    Text = '1.00'
    OnChange = Edit1Change
  end
  object Edit2: TEdit
    Left = 864
    Top = 112
    Width = 49
    Height = 21
    Color = clScrollBar
    TabOrder = 2
    Text = '1.50'
    OnChange = Edit2Change
  end
  object Edit3: TEdit
    Left = 944
    Top = 112
    Width = 49
    Height = 21
    Color = clScrollBar
    TabOrder = 3
    Text = '1.70'
    OnChange = Edit3Change
  end
  object Edit4: TEdit
    Left = 1208
    Top = 88
    Width = 49
    Height = 21
    TabOrder = 4
    Text = '2.25'
    OnChange = Edit4Change
  end
  object Edit5: TEdit
    Left = 1208
    Top = 136
    Width = 89
    Height = 21
    TabOrder = 5
    Text = '2.89'
    OnChange = Edit5Change
  end
  object Edit6: TEdit
    Left = 1024
    Top = 112
    Width = 49
    Height = 21
    TabOrder = 6
    Text = '1'
  end
  object Edit7: TEdit
    Left = 1096
    Top = 112
    Width = 49
    Height = 21
    TabOrder = 7
    Text = '4'
  end
  object Edit8: TEdit
    Left = 864
    Top = 200
    Width = 49
    Height = 21
    Color = clScrollBar
    TabOrder = 8
    Text = '1.50'
  end
  object Edit9: TEdit
    Left = 944
    Top = 200
    Width = 49
    Height = 21
    Color = clScrollBar
    TabOrder = 9
    Text = '1.70'
  end
  object Edit10: TEdit
    Left = 1024
    Top = 200
    Width = 49
    Height = 21
    Color = clScrollBar
    TabOrder = 10
    Text = '1'
  end
  object Edit11: TEdit
    Left = 1096
    Top = 200
    Width = 49
    Height = 21
    TabOrder = 11
    Text = '4'
  end
  object Edit12: TEdit
    Left = 864
    Top = 152
    Width = 49
    Height = 21
    Color = clWhite
    TabOrder = 12
    Text = '1.6'
  end
  object Edit13: TEdit
    Left = 944
    Top = 152
    Width = 49
    Height = 21
    TabOrder = 13
    Text = '0.25'
  end
  object Edit14: TEdit
    Left = 1024
    Top = 152
    Width = 49
    Height = 21
    Color = clScrollBar
    TabOrder = 14
    Text = '4'
  end
  object Memo1: TMemo
    Left = 56
    Top = 472
    Width = 769
    Height = 145
    Lines.Strings = (
      ''
      ''
      ''
      ''
      ''
      ''
      ''
      ''
      ''
      ''
      ''
      ''
      '')
    TabOrder = 15
  end
  object TrackBar1: TTrackBar
    Left = 864
    Top = 320
    Width = 41
    Height = 305
    Max = 180
    Orientation = trVertical
    Position = 45
    TabOrder = 16
    OnChange = TrackBar1Change
  end
  object TrackBar2: TTrackBar
    Left = 912
    Top = 320
    Width = 41
    Height = 305
    Max = 180
    Min = -180
    Orientation = trVertical
    Position = 90
    TabOrder = 17
    OnChange = TrackBar2Change
  end
  object Edit15: TEdit
    Left = 848
    Top = 624
    Width = 49
    Height = 21
    TabOrder = 18
    Text = '45'
  end
  object Edit16: TEdit
    Left = 912
    Top = 624
    Width = 49
    Height = 21
    TabOrder = 19
    Text = '90'
  end
  object Edit17: TEdit
    Left = 32
    Top = 272
    Width = 49
    Height = 21
    TabOrder = 20
    Text = '0.01'
  end
  object Edit18: TEdit
    Left = 784
    Top = 272
    Width = 49
    Height = 21
    TabOrder = 21
    Text = '8'
  end
  object TrackBar3: TTrackBar
    Left = 20
    Top = 224
    Width = 820
    Height = 33
    Max = 800
    Position = 392
    TabOrder = 22
    OnChange = TrackBar3Change
  end
  object Edit19: TEdit
    Left = 392
    Top = 264
    Width = 153
    Height = 21
    TabOrder = 23
    Text = '3.92'
  end
  object Edit20: TEdit
    Left = 992
    Top = 624
    Width = 49
    Height = 21
    TabOrder = 24
    Text = ' 90'
  end
  object TrackBar4: TTrackBar
    Left = 1000
    Top = 320
    Width = 41
    Height = 305
    Max = 180
    Orientation = trVertical
    Position = 90
    TabOrder = 25
    OnChange = TrackBar4Change
  end
  object Edit21: TEdit
    Left = 1208
    Top = 112
    Width = 89
    Height = 21
    TabOrder = 26
    Text = '1'
    OnChange = Edit21Change
  end
  object Edit22: TEdit
    Left = 1208
    Top = 160
    Width = 49
    Height = 21
    TabOrder = 27
    Text = '1'
    OnChange = Edit22Change
  end
  object Memo2: TMemo
    Left = 1240
    Top = 320
    Width = 25
    Height = 193
    Lines.Strings = (
      '1'
      '3'
      '1'
      '0'
      '0'
      '0'
      '0'
      '0'
      '0'
      '0'
      '0'
      '0'
      '0'
      '0'
      '')
    TabOrder = 28
  end
  object Button1: TButton
    Left = 1008
    Top = 24
    Width = 65
    Height = 41
    Caption = 'MFin'
    TabOrder = 29
    OnClick = Button1Click
  end
  object Button2: TButton
    Left = 1216
    Top = 24
    Width = 65
    Height = 41
    Caption = 'printV'
    TabOrder = 30
    OnClick = Button2Click
  end
  object TrackBar5: TTrackBar
    Left = 24
    Top = 296
    Width = 25
    Height = 177
    Max = 20
    Min = 1
    Orientation = trVertical
    Position = 20
    TabOrder = 31
    OnChange = TrackBar5Change
  end
  object Button3: TButton
    Left = 1088
    Top = 24
    Width = 73
    Height = 41
    Caption = 'Gr_P'
    TabOrder = 32
    OnClick = Button3Click
  end
  object Button4: TButton
    Left = 1176
    Top = 32
    Width = 33
    Height = 33
    Caption = 'Pr_Mtr'
    TabOrder = 33
    OnClick = Button4Click
  end
  object TrackBar6: TTrackBar
    Left = 1056
    Top = 320
    Width = 33
    Height = 305
    Max = 100
    Orientation = trVertical
    Position = 50
    TabOrder = 34
    OnChange = TrackBar6Change
  end
  object Edit23: TEdit
    Left = 1056
    Top = 624
    Width = 41
    Height = 21
    TabOrder = 35
    Text = '1'
  end
  object Memo3: TMemo
    Left = 864
    Top = 248
    Width = 177
    Height = 33
    Lines.Strings = (
      'Vx           0.70711           0.00000 *i'
      'Vy          -0.00000           0.70711 *i')
    TabOrder = 36
  end
  object Button5: TButton
    Left = 864
    Top = 288
    Width = 73
    Height = 33
    Caption = 'Reset'
    TabOrder = 37
    OnClick = Button5Click
  end
  object StaticText1: TStaticText
    Left = 1104
    Top = 328
    Width = 44
    Height = 17
    Caption = '0 Border'
    TabOrder = 38
  end
  object StaticText2: TStaticText
    Left = 1104
    Top = 344
    Width = 39
    Height = 17
    Caption = '1 ChLC'
    TabOrder = 39
  end
  object StaticText3: TStaticText
    Left = 1104
    Top = 360
    Width = 58
    Height = 17
    Caption = '2 Pol.rotate'
    TabOrder = 40
  end
  object StaticText4: TStaticText
    Left = 1104
    Top = 377
    Width = 67
    Height = 17
    Caption = '3 Linear layer'
    TabOrder = 41
  end
  object StaticText5: TStaticText
    Left = 1104
    Top = 392
    Width = 117
    Height = 17
    Caption = '4 ChLC (variable length)'
    TabOrder = 42
  end
end
