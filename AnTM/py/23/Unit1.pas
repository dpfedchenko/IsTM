
unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, ExtCtrls, ComCtrls;

type
  TForm1 = class(TForm)
    Image1: TImage;
    BitBtn1: TBitBtn;
    Edit1: TEdit;
    Label1: TLabel;
    Edit2: TEdit;
    Label2: TLabel;
    Edit3: TEdit;
    Label3: TLabel;
    Edit4: TEdit;
    Label4: TLabel;
    Edit5: TEdit;
    Label5: TLabel;
    Edit6: TEdit;
    Label6: TLabel;
    Edit7: TEdit;
    Label7: TLabel;
    Edit8: TEdit;
    Label8: TLabel;
    Edit9: TEdit;
    Label9: TLabel;
    Edit10: TEdit;
    Label10: TLabel;
    Edit11: TEdit;
    Label11: TLabel;
    Edit12: TEdit;
    Label12: TLabel;
    Edit13: TEdit;
    Label13: TLabel;
    Edit14: TEdit;
    Label14: TLabel;
    Memo1: TMemo;
    TrackBar1: TTrackBar;
    TrackBar2: TTrackBar;
    Edit15: TEdit;
    Edit16: TEdit;
    Edit17: TEdit;
    Edit18: TEdit;
    TrackBar3: TTrackBar;
    Edit19: TEdit;
    Edit20: TEdit;
    TrackBar4: TTrackBar;
    Label15: TLabel;
    Label16: TLabel;
    Label17: TLabel;
    Edit21: TEdit;
    Edit22: TEdit;
    Memo2: TMemo;
    Image2: TImage;
    Button1: TButton;
    Button2: TButton;
    TrackBar5: TTrackBar;
    Label18: TLabel;
    Label19: TLabel;
    Button3: TButton;
    Button4: TButton;
    TrackBar6: TTrackBar;
    Edit23: TEdit;
    Memo3: TMemo;
    Button5: TButton;
    StaticText1: TStaticText;
    StaticText2: TStaticText;
    StaticText3: TStaticText;
    StaticText4: TStaticText;
    StaticText5: TStaticText;
    procedure BitBtn1Click(Sender: TObject);
    procedure TrackBar1Change(Sender: TObject);
    procedure TrackBar2Change(Sender: TObject);
    procedure TrackBar3Change(Sender: TObject);
    procedure TrackBar4Change(Sender: TObject);
    procedure Edit2Change(Sender: TObject);
    procedure Edit3Change(Sender: TObject);
    procedure Edit4Change(Sender: TObject);
    procedure Edit5Change(Sender: TObject);
    procedure Edit22Change(Sender: TObject);
    procedure Edit21Change(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure TrackBar5Change(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Edit1Change(Sender: TObject);
    procedure TrackBar6Change(Sender: TObject);
    procedure Button5Click(Sender: TObject);
    

  private
    { Private declarations }
  public
    { Public declarations }
  end;
type TMtr=array[1..4,1..4,1..2] of double;
     TVct=array[1..4,1..2] of double;
var
  Form1: TForm1;
  M_t,M_p: array[0..10000] of double;
  VecGr: array[1..4,1..100,1..2] of double;
  M_a:array[0..800] of double;
  N,Mfin: TMtr;
  Gr_L,Gr_P,MDS,GrTmp,PhsTmp,Zero:TMtr;
  MLD,ML,MF,MsF,MsL,MF1,GL_Ch_I:TMtr;
  Nv,No,Ne,D_D:double;
  epsilon_o,mu_o,epsilon_e,mu_e:double;
  Rx_r,Rx_i,Ry_r,Ry_i,Tx_r,Tx_i,Ty_r,Ty_i:double;
  Ax_r,Ax_i,Ay_r,Ay_i:double;
  Wmin,Wmax,Wloc:double;
  code:integer;
  Lo,L,Ld,Theta,c,Nd,omega,L1,L2:double;
  Lo1,Lo2:double;
  TS_t,TS_r,SuS:double;
  sloy:array[0..10] of integer;
  V,Vtemp:TVct;
  myFile:TextFile;
  PrnFlg:boolean;
  RhoPh,iota_r:double;
const
  Pi=3.14159265358979323846264338328;
  S2=1.41421356237309504880168872421;
  implementation

{$R *.dfm}
procedure print_Matr(var Mpr: TMtr;NNN:string);
var
st1,st2,st3,st4,st5:string;
Ii,Ij,LL:integer;
begin



writeln(MyFile,NNN);
For Ii:= 1 To 4 do begin
   st2:='';
   st4:='|';
    For Ij := 1 To 4 do begin
        str(Mpr[Ii,Ij,1]:18:15,st1);
        str(Mpr[Ii,Ij,2]:18:15,st3);

        if  (Mpr[Ii,Ij,2]<0) then st5:='' else begin
                                                st5:='+';
                                               delete(st3,1,1);
                                               end;

        st2:=st2+st1+st5+st3+'*I'+', ';
                        end;
                        LL:=length(st2);
                        delete(st2,LL-1,1);
                        writeln(MyFile,st2);
                       end;
end;

procedure ZeroFin();
var
Ii,Ij:integer;
begin
For Ii := 1 To 4 do begin
    For Ij := 1 To 4 do begin
       Mfin[Ii,Ij,1]:=0;
       Mfin[Ii,Ij,2]:=0;
       Zero[Ii,Ij,1]:=0;
                        end;
    Mfin[Ii,Ii,1]:=1;
                    end;
end;

function MVc(var  Mpr:TMtr; Vpr:TVct):TVct;
var
t_r,t_i :double;
Ii,Ij,Ik: integer;
Vp:array[1..4,1..2] of double;
begin
For Ii := 1 To 4 do begin
     t_r := 0; t_i := 0; {Обнуляем временные переменные}
        For Ik := 1 To 4 do begin
            t_r := t_r + Vpr[Ik,1] * Mpr[Ii, Ik,1] - Vpr[Ik,2] * Mpr[Ii, Ik,2];
            t_i := t_i + Vpr[Ik,1] * Mpr[Ii, Ik,2] + Vpr[Ik,2] * Mpr[Ii, Ik,1];
                           end;
        Vp[Ii,1] := t_r;
        Vp[Ii,2] := t_i;

                    end;

 For Ii := 1 To 4 do begin
                      MVc[Ii,1] := Vp[Ii,1];
                      MVc[Ii,2] := Vp[Ii,2];
                     end;

end;

function AbsVec(var Vinp:TVct):double;{Возвращение квадрата модуля комплексного вектора}
begin

AbsVec:=sqr(Vinp[1,1])+sqr(Vinp[1,2])+sqr(Vinp[2,1])+sqr(Vinp[2,2])+sqr(Vinp[3,1])+sqr(Vinp[3,2])+sqr(Vinp[4,1])+sqr(Vinp[4,2]);

end;

function MMc(var N_1,N_2:TMtr):Tmtr;
var
t_r,t_i :double;
Ii,Ij,Ik: integer;
T1:array[1..4,1..4,1..2] of double;

begin
For Ii := 1 To 4 do begin
    For Ij := 1 To 4 do begin
        t_r := 0; t_i := 0; {Обнуляем временные переменные}
        For Ik := 1 To 4 do begin
            t_r := t_r + N_1[Ii, Ik,1] * N_2[Ik, Ij,1] - N_1[Ii, Ik,2] * N_2[Ik, Ij,2];
            t_i := t_i + N_1[Ii, Ik,1] * N_2[Ik, Ij,2] + N_1[Ii, Ik,2] * N_2[Ik, Ij,1];
                           end;
        T1[Ii, Ij,1] := t_r;
        T1[Ii, Ij,2] := t_i;
                       end;
                    end;

 For Ii := 1 To 4 do begin
    For Ij := 1 To 4 do begin
        MMc[Ii, Ij,1] := T1[Ii, Ij,1];
        MMc[Ii, Ij,2] := T1[Ii, Ij,2];
                       end;
                    end;
end;





procedure GR_MTRX(eo_l,mo_l,ee_l,me_l,eo_p,mo_p,ee_p,me_p:double);{Матрица граничного отражения 4х4}
var
Ko,Ke:double;
st1,st2,st3,st4:string;
Ii,Ij:integer;
begin
Ko:=sqrt(mo_l/mo_p*eo_p/eo_l);
Ke:=sqrt(me_l/me_p*ee_p/ee_l);

GrTmp[1,1,1]:=(1+Ko)/2;GrTmp[1,2,1]:=(1-Ko)/2;GrTmp[1,3,1]:=0;GrTmp[1,4,1]:=0;
GrTmp[2,1,1]:=(1-Ko)/2;GrTmp[2,2,1]:=(1+Ko)/2;GrTmp[2,3,1]:=0;GrTmp[2,4,1]:=0;
GrTmp[3,1,1]:=0;GrTmp[3,2,1]:=0;GrTmp[3,3,1]:=(1+Ke)/2;GrTmp[3,4,1]:=(1-Ke)/2;
GrTmp[4,1,1]:=0;GrTmp[4,2,1]:=0;GrTmp[4,3,1]:=(1-Ke)/2;GrTmp[4,4,1]:=(1+Ke)/2;

end;

procedure POV_MTRX(eo_l,mo_l,ee_l,me_l,eo_p,mo_p,ee_p,me_p:double);{Матрица граничного отражения 4х4}
var
Ko,Ke:double;
st1,st2,st3,st4:string;
Ii,Ij:integer;
begin



Ko:=sqrt(mo_l/mo_p*eo_p/eo_l);
Ke:=sqrt(me_l/me_p*ee_p/ee_l);

MDS[1,1,1]:=(1+Ko)/2;MDS[1,2,1]:=(1-Ko)/2;MDS[1,3,1]:=0;MDS[1,4,1]:=0;
MDS[2,1,1]:=(1-Ko)/2;MDS[2,2,1]:=(1+Ko)/2;GrTmp[2,3,1]:=0;MDS[2,4,1]:=0;
MDS[3,1,1]:=0;MDS[3,2,1]:=0;MDS[3,3,1]:=(1+Ke)/2;MDS[3,4,1]:=(1-Ke)/2;
MDS[4,1,1]:=0;MDS[4,2,1]:=0;MDS[4,3,1]:=(1-Ke)/2;MDS[4,4,1]:=(1+Ke)/2;

end;



procedure PHS_MTRX(eo,mo,ee,me,omega,z:double);{Матрица фазового набега 4х4}
var
Ko,Ke:double;
begin
Ko:=sqrt(mo*eo)*omega;Ke:=sqrt(me*ee)*omega;
{(1,1) = exp(-I*No*z), (2,2) =exp(I*No*z), (3,3) =exp(-I*Ne*z), (4,4) = exp(I*Ne*z){}
PhsTmp[1,1,1]:=cos(Ko*z);PhsTmp[1,2,1]:=0;PhsTmp[1,3,1]:=0;PhsTmp[1,4,1]:=0;
PhsTmp[1,1,2]:=-sin(Ko*z);PhsTmp[1,2,2]:=0;PhsTmp[1,3,2]:=0;PhsTmp[1,4,2]:=0;

PhsTmp[2,1,1]:=0;PhsTmp[2,2,1]:=cos(Ko*z);PhsTmp[2,3,1]:=0;PhsTmp[2,4,1]:=0;
PhsTmp[2,1,2]:=0;PhsTmp[2,2,2]:=sin(Ko*z);PhsTmp[2,3,2]:=0;PhsTmp[2,4,2]:=0;

PhsTmp[3,1,1]:=0;PhsTmp[3,2,1]:=0;PhsTmp[3,3,1]:=cos(Ke*z);PhsTmp[3,4,1]:=0;
PhsTmp[3,1,2]:=0;PhsTmp[3,2,2]:=0;PhsTmp[3,3,2]:=-sin(Ke*z);PhsTmp[3,4,2]:=0;

PhsTmp[4,1,1]:=0;PhsTmp[4,2,1]:=0;PhsTmp[4,3,1]:=0;PhsTmp[4,4,1]:=cos(Ke*z);
PhsTmp[4,1,2]:=0;PhsTmp[4,2,2]:=0;PhsTmp[4,3,2]:=0;PhsTmp[4,4,2]:=sin(Ke*z);

end;



procedure InitMtx(N_v:double); {Инициализация мартиц, не зависящих от omega}
var
Ii,Ij,Ik: integer;
mu_o_0_5,epsilon_o_0_5: double;
t1,t2,t3,t4,t5,t6,t7,t8,t9,t10:double;
t11,t12,t13,t14,t15,t16,t17,t18,t19,t20:double;
t21,t22,t23,t24,t25,t26,t27,t28,t29,t30:double;
st2:string;
begin


Ne:=sqrt(mu_e*epsilon_e);



For Ii := 1 To 4 do begin
    For Ij := 1 To 4 do begin
       MDS[Ii,Ij,2]:=0;
       MDS[Ii,Ij,1]:=0;
       Mfin[Ii,Ij,1]:=0;
       Mfin[Ii,Ij,2]:=0;
                        end;
    Mfin[Ii,Ii,1]:=1;
                    end;


t1:=cos(D_D);
t2:=sin(D_D);

MDS[1,1,1]:=t1;
MDS[2,2,1]:=t1;
MDS[3,3,1]:=t1;
MDS[4,4,1]:=t1;
{MDS[1,1,2]:=t1;
MDS[2,2,2]:=t1;
MDS[3,3,2]:=t1;
MDS[4,4,2]:=t1;{}




MDS[1,3,1]:=-t2;
MDS[2,4,1]:=-t2;
MDS[3,1,1]:=t2;
MDS[4,2,1]:=t2;
{MDS[1,3,2]:=-t2;
MDS[2,4,2]:=-t2;
MDS[3,1,2]:=t2;
MDS[4,2,2]:=t2;{}



end;


function MFc(var LL,LoL,omega:double):TMtr;{Заполнение матрицы MF - херального слоя}
var
xi,X_M,A,B:double;
SS,CS,DifC,DifS,SumC,SumS,EI,SI,CI:double;
Lp,NLW,iota,sigma,SqS,R1,S1:double;
p1,p2,p3,p4,p5,p6:double;

begin

xi:=mu_e*No/(mu_o*Ne);
X_M:=(xi+1/xi);

A:=2*sqrt(sqr(sqr(Ne)-sqr(No))+16*sqr(Pi)/sqr(LoL*omega)*(sqr(No)+Ne*No*X_M+sqr(Ne)));


B:=2*(sqr(No)+sqr(Ne)+8*sqr(Pi/(omega*LoL)));

iota := Sqrt(Abs(A-B));
sigma := Sqrt(A+B);

Lp:=LL*omega/2;
If (a - b) < 0 Then begin
    CI := Cos(Lp * iota);
    SI := Sin(Lp * iota) / iota;
    iota_r:=0;
                       end
                 Else begin
    EI := Exp(Lp * iota);
    CI := 1 / 2 * (EI + 1 / EI);
    if iota=0 then SI:=Lp else SI := (1 / 2 * (EI - 1 / EI)) / iota;
    iota_r:=iota;
                       end;
CS := Cos(Lp * sigma);
SS := Sin(Lp * sigma) / sigma;

DifC := CI - CS;DifS := SI - SS;SumC := CS + CI;SumS := SS + SI;

MFc[1,1,1]:= 1/2/A*(2*sqr(No)*DifC+A*SumC-2*sqr(Ne)*DifC);
MFc[1,2,1]:= 0;
MFc[1,3,1]:= (-2*sqr(No+Ne)*DifS+A*SumS)*Pi*(2+X_M)/LoL/omega/A/(xi+1);
MFc[1,4,1]:= (X_M-2)*(-2*sqr(Ne-No)*DifS+A*SumS)*Pi/LoL/omega/A/(-1+xi);
MFc[2,1,1]:= 0;
MFc[2,2,1]:= 1/2/A*(2*sqr(No)*DifC+A*SumC-2*sqr(Ne)*DifC);
MFc[2,3,1]:= 2*(xi-1/2*X_M)*(-2*sqr(Ne-No)*DifS+A*SumS)*Pi/LoL/omega/A/(xi+1);
MFc[2,4,1]:= 2*(xi-1/2*X_M)*(-2*sqr(No+Ne)*DifS+A*SumS)*Pi/LoL/omega/A/(-1+xi);
MFc[3,1,1]:= -(-2*sqr(No+Ne)*DifS+A*SumS)*Pi*(xi+1)/LoL/omega/A;
MFc[3,2,1]:= (X_M-2)*(-2*sqr(Ne-No)*DifS+A*SumS)*Pi*(xi+1)/LoL/omega/A/(2*xi-X_M);
MFc[3,3,1]:= 1/2/A*(2*sqr(Ne)*DifC-2*sqr(No)*DifC+A*SumC);
MFc[3,4,1]:= 0;
MFc[4,1,1]:= (-2*sqr(Ne-No)*DifS+A*SumS)*(-1+xi)*Pi/LoL/omega/A;
MFc[4,2,1]:= -(-2*sqr(No+Ne)*DifS+A*SumS)*(-1+xi)*Pi*(2+X_M)/LoL/omega/A/(2*xi-X_M);
MFc[4,3,1]:= 0;
MFc[4,4,1]:= 1/2/A*(2*sqr(Ne)*DifC-2*sqr(No)*DifC+A*SumC);

MFc[1,1,2]:= 1/2*((-2*X_M*No*sqr(Ne)+(-8*sqr(No)+2*B)*Ne+X_M*(-2*sqr(No)+B)*No)*DifS-2*Ne*A*SumS)/A;
MFc[1,2,2]:= -1/2*DifS*(-2*sqr(Ne)+B-2*sqr(No))*No*(2+X_M)*(X_M-2)/A/(2*xi-X_M);
MFc[1,3,2]:= -2*Pi*(2+X_M)*DifC*(No+Ne)/LoL/omega/A/(xi+1);
MFc[1,4,2]:= -2*Pi*(X_M-2)*DifC*(Ne-No)/LoL/omega/A/(-1+xi);
MFc[2,1,2]:= DifS*No*(xi-1/2*X_M)*(-2*sqr(Ne)+B-2*sqr(No))/A;
MFc[2,2,2]:= 1/2*((2*X_M*No*sqr(Ne)+(8*sqr(No)-2*B)*Ne-X_M*(-2*sqr(No)+B)*No)*DifS+2*Ne*A*SumS)/A;
MFc[2,3,2]:= 4*(xi-1/2*X_M)*DifC*Pi*(Ne-No)/LoL/omega/A/(xi+1);
MFc[2,4,2]:= 4*(xi-1/2*X_M)*DifC*(No+Ne)*Pi/LoL/omega/A/(-1+xi);
MFc[3,1,2]:= 2*Pi*(xi+1)*DifC*(No+Ne)/LoL/omega/A;
MFc[3,2,2]:= 2*Pi*(xi+1)*(X_M-2)*DifC*(Ne-No)/LoL/omega/A/(2*xi-X_M);
MFc[3,3,2]:= 1/2*((-2*X_M*Ne*sqr(Ne)-8*No*sqr(Ne)+(-2*sqr(No)+B)*X_M*Ne+2*No*B)*DifS-2*No*A*SumS)/A;
MFc[3,4,2]:= (1/2*X_M-1)*DifS*Ne*(-2*sqr(Ne)+B-2*sqr(No))*(xi+1)/A/(-1+xi);
MFc[4,1,2]:= -2*Pi*(-1+xi)*DifC*(Ne-No)/LoL/omega/A;
MFc[4,2,2]:= -2*(-1+xi)*Pi*(2+X_M)*DifC*(No+Ne)/LoL/omega/A/(2*xi-X_M);
MFc[4,3,2]:= -1/2*Ne*(-1+xi)*DifS*(-2*sqr(Ne)+B-2*sqr(No))*(2+X_M)/A/(xi+1);
MFc[4,4,2]:= 1/2*((2*X_M*Ne*sqr(Ne)+8*No*sqr(Ne)-(-2*sqr(No)+B)*X_M*Ne-2*No*B)*DifS+2*No*A*SumS)/A;


end;



function MLDc(var Ld1,omega,Nd:double):TMtr;{Заполнение матрицы MLD - изотропного слоя}

begin
MLDc[1,1,1] := Cos(Nd * Ld1 * omega);
MLDc[1,1,2] := -Sin(Nd * Ld1 * omega);;
MLDc[1,2,1] := 0;
MLDc[1,2,2] := 0;
MLDc[1,3,1] := 0;
MLDc[1,3,2] := 0;
MLDc[1,4,1] := 0;
MLDc[1,4,2] := 0;
MLDc[2,1,1] := 0;
MLDc[2,1,2] := 0;
MLDc[2,2,1] := Cos(Nd * Ld1 * omega);
MLDc[2,2,2] := Sin(Nd * Ld1 * omega);
MLDc[2,3,1] := 0;
MLDc[2,3,2] := 0;
MLDc[2,4,1] := 0;
MLDc[2,4,2] := 0;
MLDc[3,1,1] := 0;
MLDc[3,1,2] := 0;
MLDc[3,2,1] := 0;
MLDc[3,2,2] := 0;
MLDc[3,3,1] := Cos(Nd * Ld1 * omega);
MLDc[3,3,2] := -Sin(Nd * Ld1 * omega);
MLDc[3,4,1] := 0;
MLDc[3,4,2] := 0;
MLDc[4,1,1] := 0;
MLDc[4,1,2] := 0;
MLDc[4,2,1] := 0;
MLDc[4,2,2] := 0;
MLDc[4,3,1] := 0;
MLDc[4,3,2] := 0;
MLDc[4,4,1] := Cos(Nd * Ld1 * omega);
MLDc[4,4,2] := Sin(Nd * Ld1 * omega);
end;





procedure Ampl();
var
nrx_r,nrx_i,nry_r,nry_i,ntx_r,ntx_i,nty_r,nty_i,d_r,d_i:double;
Den_f:double;
begin
nrx_r := (-Mfin[3,3,1] * Ax_i - Mfin[3,3,2] * Ax_r + Ay_r * Mfin[1,3,2] + Ay_i * Mfin[1,3,1] ) * Mfin[2,1,2] + (Ax_r * Mfin[3,1,2] - Mfin[1,1,1] * Ay_i + Ax_i * Mfin[3,1,1] - Mfin[1,1,2] * Ay_r) * Mfin[2,3,2] + (Mfin[3,3,1] * Ax_r - Mfin[3,3,2] * Ax_i - Ay_r * Mfin[1,3,1] + Ay_i * Mfin[1,3,2] ) * Mfin[2,1,1] + Mfin[2,3,1] * (-Ax_r * Mfin[3,1,1] + Mfin[1,1,1] * Ay_r + Ax_i * Mfin[3,1,2] - Mfin[1,1,2] * Ay_i);
nrx_i := (Mfin[3,3,1] * Ax_r - Mfin[3,3,2] * Ax_i - Ay_r * Mfin[1,3,1] + Ay_i * Mfin[1,3,2] ) * Mfin[2,1,2] + (-Ax_r * Mfin[3,1,1] + Mfin[1,1,1] * Ay_r + Ax_i * Mfin[3,1,2] - Mfin[1,1,2] * Ay_i) * Mfin[2,3,2] + (Mfin[3,3,1] * Ax_i + Mfin[3,3,2] * Ax_r - Ay_r * Mfin[1,3,2] - Ay_i * Mfin[1,3,1] ) * Mfin[2,1,1] - Mfin[2,3,1] * (Ax_r * Mfin[3,1,2] - Mfin[1,1,1] * Ay_i + Ax_i * Mfin[3,1,1] - Mfin[1,1,2] * Ay_r);
nry_r := (Mfin[3,3,1] * Ax_i + Mfin[3,3,2] * Ax_r - Ay_r * Mfin[1,3,2] - Ay_i * Mfin[1,3,1] ) * Mfin[4,1,2] + (-Ax_i * Mfin[3,1,1] + Mfin[1,1,2] * Ay_r + Mfin[1,1,1] * Ay_i - Ax_r * Mfin[3,1,2]) * Mfin[4,3,2] + (-Mfin[3,3,1] * Ax_r + Mfin[3,3,2] * Ax_i + Ay_r * Mfin[1,3,1] - Ay_i * Mfin[1,3,2] ) * Mfin[4,1,1] - Mfin[4,3,1] * (-Ax_r * Mfin[3,1,1] + Mfin[1,1,1] * Ay_r + Ax_i * Mfin[3,1,2] - Mfin[1,1,2] * Ay_i);
nry_i:= (-Mfin[3,3,1] * Ax_r + Mfin[3,3,2] * Ax_i + Ay_r * Mfin[1,3,1] - Ay_i * Mfin[1,3,2] ) * Mfin[4,1,2] + (-Ax_i * Mfin[3,1,2] + Mfin[1,1,2] * Ay_i - Mfin[1,1,1] * Ay_r + Ax_r * Mfin[3,1,1]) * Mfin[4,3,2] + (-Mfin[3,3,1] * Ax_i - Mfin[3,3,2] * Ax_r + Ay_r * Mfin[1,3,2] + Ay_i * Mfin[1,3,1] ) * Mfin[4,1,1] + Mfin[4,3,1] * (Ax_r * Mfin[3,1,2] - Mfin[1,1,1] * Ay_i + Ax_i * Mfin[3,1,1] - Mfin[1,1,2] * Ay_r);

ntx_r := Mfin[3,3,1] * Ax_r - Mfin[3,3,2] * Ax_i - Ay_r * Mfin[1,3,1] + Ay_i * Mfin[1,3,2] ;
ntx_i := Mfin[3,3,1] * Ax_i + Mfin[3,3,2] * Ax_r - Ay_r * Mfin[1,3,2] - Ay_i * Mfin[1,3,1] ;
nty_r := -Ax_i * Mfin[3,1,2] + Mfin[1,1,2] * Ay_i - Mfin[1,1,1] * Ay_r + Ax_r * Mfin[3,1,1];
nty_i := Ax_r * Mfin[3,1,2] - Mfin[1,1,1] * Ay_i + Ax_i * Mfin[3,1,1] - Mfin[1,1,2] * Ay_r;

d_r := Mfin[1,1,1] * Mfin[3,3,1] - Mfin[1,1,2] * Mfin[3,3,2] - Mfin[1,3,1] * Mfin[3,1,1] + Mfin[1,3,2] * Mfin[3,1,2];
d_i := Mfin[1,1,1] * Mfin[3,3,2] + Mfin[1,1,2] * Mfin[3,3,1] - Mfin[1,3,1] * Mfin[3,1,2] - Mfin[1,3,2] * Mfin[3,1,1];

Den_f := 1 / (d_r * d_r + d_i * d_i+0.00000001);

Rx_r := (nrx_r * d_r + nrx_i * d_i) * Den_f;
Rx_i := (-nrx_r * d_i + nrx_i * d_r) * Den_f;

Ry_r := -(nry_r * d_r + nry_i * d_i) * Den_f;
Ry_i := -(-nry_r * d_i + nry_i * d_r) * Den_f;

Tx_r := (ntx_r * d_r + ntx_i * d_i) * Den_f;
Tx_i := (-ntx_r * d_i + ntx_i * d_r) * Den_f;

Ty_r := -(nty_r * d_r + nty_i * d_i) * Den_f;
Ty_i := -(-nty_r * d_i + nty_i * d_r) * Den_f;
end;



procedure MulM();
var
Isl,mu,Nom_gr,Ii,Ij,Isl2:integer;
flg:boolean;
st1:string;
Eo_old,Ho_old,Ee_old,He_old:double;
Eo_new,Ho_new,Ee_new,He_new,AA1,AA2:double;
Ei,Ci,Si:double;
Ar_Mt: array [1..4,1..4,1..2,1..10] of double;
ar_indx:integer;
Ar_I: array [0..10] of integer;
Mtemp,mfin1:TMtr;
Vtemp:TVct;
t1,t2,t3,t4:double;
iota_r1,iota_r4:double;

begin

InitMtx(Nv);

MF:=MFc(L1,Lo1,omega);
iota_r1:=iota_r;
MF1:=MFc(L2,Lo1,omega);
iota_r4:=iota_r;

 if (PrnFlg) then begin
                            writeln(MyFile,'L1',L1);
                            writeln(MyFile,'L2',L2);

                          end;


ML:=MLDc(Ld,omega,Nd);

flg:=true;
ZeroFin;  {Матрица Mfin делается реальной единичной}
Eo_old:=Nv*Nv;Ho_old:=1;Ee_old:=Nv*Nv;He_old:=1;{Начальные (справа) показатели преломления}


{if PrnFlg then print_matr(MF,'MF');{}
if PrnFlg then begin
                writeln(MyFile,'--------------------MulM--------------------------');
                print_matr(MDS,'MDS');{**********************************}
                print_matr(Mfin,'Begin');{**********************************}
               end;

for Isl:=0 to 10 do begin
 if flg then
 case sloy[Isl] of
 0: begin flg:=false;
          GR_MTRX(Nv*Nv,1,Nv*Nv,1,Eo_old,Ho_old,Ee_old,He_old);
           if (PrnFlg) then begin
                            writeln(MyFile,'G0');
                            print_matr(GrTmp,'Gr_tmp0');
                          end;

          Mfin:=MMc(GrTmp,Mfin);
          if (PrnFlg) then begin
                            writeln(MyFile,0);
                            print_matr(Mfin,'Gr');
                           end;
          Ar_I[Isl]:=0;
          for Ii:=1 to 4 do
          for ij:=1 to 4 do begin
                            Ar_mt[Ii,Ij,1,Isl]:=Mfin[Ii,Ij,1];
                            Ar_mt[Ii,Ij,2,Isl]:=Mfin[Ii,Ij,2];
                            end;

    end;
 1: begin GR_MTRX(epsilon_o,mu_o,epsilon_e,mu_e,Eo_old,Ho_old,Ee_old,He_old);
                     if (PrnFlg) then begin
                            writeln(MyFile,'G1');
                            print_matr(GrTmp,'Gr_tmp1');
                          end;

          Mfin:=MMc(GrTmp,Mfin);
          if (PrnFlg) then begin
                            writeln(MyFile,1);
                            print_matr(Mfin,'Gr_mfin1');
                           end;
          Eo_old:=epsilon_o;
          Ho_old:=mu_o;
          Ee_old:=epsilon_e;
          He_old:=mu_e;
{          if (PrnFlg) then print_matr(MF,'MF'); {}
          Mfin:=MMc(MF,Mfin);
          if (PrnFlg) then begin
                            print_matr(MF,'MF');
                            print_matr(Mfin,'MFin_pr1');
                           end;
          Ar_I[Isl]:=1;
          for Ii:=1 to 4 do
          for ij:=1 to 4 do begin
                            Ar_mt[Ii,Ij,1,Isl]:=Mfin[Ii,Ij,1];
                            Ar_mt[Ii,Ij,2,Isl]:=Mfin[Ii,Ij,2];
                            end;


    end;
 2: begin
          case sloy[Isl+1] of
          0:begin
            end;
          1:begin
          GR_MTRX(epsilon_o,mu_o,epsilon_e,mu_e,Eo_old,Ho_old,Ee_old,He_old);
          Mfin:=MMc(GrTmp,Mfin);
          Eo_old:=epsilon_o;
          Ho_old:=mu_o;
          Ee_old:=epsilon_e;
          He_old:=mu_e;
            end;

          2:begin
            end;

          3:begin
          GR_MTRX(Nd*Nd,1,Nd*Nd,1,Eo_old,Ho_old,Ee_old,He_old);
          Mfin:=MMc(GrTmp,Mfin);
          Eo_old:=Nd*Nd;
          Ho_old:=1;
          Ee_old:=Nd*Nd;
          He_old:=1;
            end;


          4:begin
          GR_MTRX(epsilon_o,mu_o,epsilon_e,mu_e,Eo_old,Ho_old,Ee_old,He_old);
          Mfin:=MMc(GrTmp,Mfin);
          Eo_old:=epsilon_o;
          Ho_old:=mu_o;
          Ee_old:=epsilon_e;
          He_old:=mu_e;
            end;

         end;{Case}
          if (PrnFlg) then print_matr(GrTmp,'Gr_Povorot');

          Mfin:=MMc(MDS,Mfin);
          if (PrnFlg) then begin
                            print_matr(MDS,'MDS Povorot');
                            print_matr(Mfin,'Mfin Povorot');
                           end;

          Ar_I[Isl]:=2;
    end;
 3: begin GR_MTRX(Nd*Nd,1,Nd*Nd,1,Eo_old,Ho_old,Ee_old,He_old);

           if (PrnFlg) then begin
                            writeln(MyFile,'G3');
                            print_matr(GrTmp,'Gr_tmp3');
                          end;

          Mfin1:=MMc(GrTmp,Mfin);
          if (PrnFlg) then begin
                            writeln(MyFile,3);
                            print_matr(Mfin1,'Gr_mfin1');
                          end;
          Eo_old:=Nd*Nd;
          Ho_old:=1;
          Ee_old:=Nd*Nd;
          He_old:=1;
          Mfin:=MMc(ML,Mfin1);
          if (PrnFlg) then begin
                            print_matr(ML,'ML');
                            print_matr(Mfin,'MFin_pr');
                           end;
          Ar_I[Isl]:=3;
          for Ii:=1 to 4 do
          for ij:=1 to 4 do begin
                            Ar_mt[Ii,Ij,1,Isl]:=Mfin1[Ii,Ij,1];
                            Ar_mt[Ii,Ij,2,Isl]:=Mfin1[Ii,Ij,2];
                            end;
    end;


4: begin GR_MTRX(epsilon_o,mu_o,epsilon_e,mu_e,Eo_old,Ho_old,Ee_old,He_old);

                     if (PrnFlg) then begin
                            writeln(MyFile,'G4');

                            print_matr(GrTmp,'Gr_tmp4');
                          end;



          Mfin:=MMc(GrTmp,Mfin);
          if (PrnFlg) then begin
                            writeln(MyFile,1);
                            print_matr(Mfin,'Gr_mfin4');
                           end;
          Eo_old:=epsilon_o;
          Ho_old:=mu_o;
          Ee_old:=epsilon_e;
          He_old:=mu_e;
          Mfin:=MMc(MF1,Mfin);
          if (PrnFlg) then begin
                            print_matr(MF1,'MF4');
                            print_matr(Mfin,'MFin_pr4');
                           end;

          Ar_I[Isl]:=1;
          for Ii:=1 to 4 do
          for ij:=1 to 4 do begin
                            Ar_mt[Ii,Ij,1,Isl]:=Mfin[Ii,Ij,1];
                            Ar_mt[Ii,Ij,2,Isl]:=Mfin[Ii,Ij,2];
                            end;
   end;
 end;



end;

Ampl;
if PrnFlg then begin
                 writeln(MyFile,'Tx ',Tx_r,' ',Tx_i,'*i');
                 writeln(MyFile,'Ty ',Ty_r,' ',Ty_i,'*i');
               end;

    TS_t := Tx_r * Tx_r + Tx_i * Tx_i + Ty_r * Ty_r + Ty_i * Ty_i;
    TS_r := Rx_r * Rx_r + Rx_i * Rx_i + Ry_r * Ry_r + Ry_i * Ry_i;
    SuS := TS_t + TS_r;
V[1,1] := Tx_r; V[1,2] := Tx_i;
V[2,1] := 0; V[2,2] := 0;
V[3,1] := Ty_r; V[3,2] := Ty_i;
V[4,1] := 0; V[4,2] := 0;

    flg:=true;
    RhoPh:=0;



 for Isl:=0 to 10 do begin
                     for Ii:=1 to 4 do
                     for ij:=1 to 4 do begin
                        Mtemp[Ii,Ij,1]:=Ar_mt[Ii,Ij,1,Isl];
                        Mtemp[Ii,Ij,2]:=Ar_mt[Ii,Ij,2,Isl];
                                       end;
 if flg then
 case sloy[Isl] of
 0: begin flg:=false;
    end;
 1: begin

    if iota_r1=0 then
                     RhoPh:=RhoPh + AbsVec(V)

                else begin
    iota_r:=iota_r1;
    EI := Exp(L1*omega/2 * iota_r);
    CI := 1 / 2 * (EI + 1 / EI);
    SI := (1 / 2 * (EI - 1 / EI));
    t1:=(sqr(V[1,2])+sqr(V[1,1])-sqr(V[2,2])-sqr(V[2,1]))*sqr(CI);
    t2:=(sqr(V[1,2])+sqr(V[1,1])+sqr(V[2,2])+sqr(V[2,1]))*SI*CI;
    t3:=sqr(V[3,2])+sqr(V[3,1])+sqr(V[4,2])+sqr(V[4,1]);
    t4:=-(sqr(V[1,2])+sqr(V[1,1])-sqr(V[2,2])-sqr(V[2,1]));
    RhoPh:=RhoPh + (t1+t2+t4)/(L1*iota_r*omega)+t3;
                     end;

    end;
 2: begin

    end;
 3: begin
    Vtemp:=MVc(Mtemp,V);
    RhoPh:=RhoPh+AbsVec(Vtemp);

    end;
 4: begin

    if iota_r4=0 then
                     RhoPh:=RhoPh + AbsVec(V)

                else begin
    iota_r:=iota_r4;
    EI := Exp(L2*omega/2 * iota_r);
    CI := 1 / 2 * (EI + 1 / EI);
    SI := (1 / 2 * (EI - 1 / EI));
    t1:=(sqr(V[1,2])+sqr(V[1,1])-sqr(V[2,2])-sqr(V[2,1]))*sqr(CI);
    t2:=(sqr(V[1,2])+sqr(V[1,1])+sqr(V[2,2])+sqr(V[2,1]))*SI*CI;
    t3:=sqr(V[3,2])+sqr(V[3,1])+sqr(V[4,2])+sqr(V[4,1]);
    t4:=-(sqr(V[1,2])+sqr(V[1,1])-sqr(V[2,2])-sqr(V[2,1]));
    RhoPh:=RhoPh + (t1+t2+t4)/(L2*iota_r*omega)+t3;
                     end;

    end;

 end;
    end;
end;


procedure InitPar();
var
Ii,Ij,Jj:integer;

st1,st2,st3,st4:string[40];
Theta1,Phi1:double;
begin

val(Form1.Edit6.Text,Lo1,code);
val(Form1.Edit10.Text,Lo2,code);
val(Form1.Edit7.Text,L1,code);
val(Form1.Edit11.Text,L2,code);
{val(Form1.Edit2.Text,No,code);
val(Form1.Edit3.Text,Ne,code);{}

{Блок считывания epsilon, mu и вычисления плказателей преломления}
val(Form1.Edit4.Text,epsilon_o,code);
val(Form1.Edit5.Text,epsilon_E,code);
val(Form1.Edit21.Text,mu_o,code);
val(Form1.Edit22.Text,mu_E,code);
No:=sqrt(mu_o*epsilon_o);
Ne:=sqrt(mu_e*epsilon_e);
{^^^^Блок считывания epsilon, mu и вычисления плказателей преломления^^^^}

val(Form1.Edit1.Text,Nv,code);
val(Form1.Edit13.Text,Ld,code);
val(Form1.Edit12.Text,Nd,code);

Theta:=0;
{D_D:=Pi/2;No := 1.7; Ne := 1.5;}
val(Form1.Edit20.Text,Phi1,code);
D_D:=Phi1/180*Pi;
c := 1; 
val(Form1.Edit15.Text,Theta1,code);
val(Form1.Edit16.Text,Phi1,code);
Ax_r:=cos(Theta1/180*Pi);
Ax_i:=0;
Ay_r:=sin(Theta1/180*Pi)*cos(Phi1/180*Pi);
Ay_i:=sin(Theta1/180*Pi)*sin(Phi1/180*Pi);



val(Form1.Edit17.Text,Wmin,code);
val(Form1.Edit18.Text,Wmax,code);{}

end;

 {******************************************************}
 {******************************************************}
 {******************************************************}
 {******************************************************}
 {******************************************************}
 {******************************************************}
procedure MainCalc();
var
Ii,Ij,Jj:integer;

st1,st2,st3,st4:string[40];
Theta1,Phi1:double;

begin
InitPar();

Form1.Image1.canvas.Brush.Color:=clWhite;
Form1.Image1.canvas.rectangle(0, 0, Form1.Image1.ClientWidth, Form1.Image1.ClientHeight);
Form1.Image1.canvas.Pen.Color:=clblue;
Form1.Image1.canvas.moveto(0,29);
Form1.Image1.canvas.lineto(Form1.Image1.ClientWidth,29);


{omega:=6.37;{}


for Jj:=0 to 10000 do begin
omega:=Wmin+Jj/10000*(Wmax-Wmin);

   MulM();

    TS_t := Tx_r * Tx_r + Tx_i * Tx_i + Ty_r * Ty_r + Ty_i * Ty_i;
    TS_r := Rx_r * Rx_r + Rx_i * Rx_i + Ry_r * Ry_r + Ry_i * Ry_i;
    SuS := TS_t + TS_r;

  {  str(TS_t:18:5,st1);
    str(TS_r:18:5,st2);
    str(SuS:18:5,st3);

 {   Form1.Memo1.Lines[0]:=st1;
    Form1.Memo1.Lines[1]:=st2;
    Form1.Memo1.Lines[2]:=st3;{}

  M_t[Jj]:=TS_t;
  form1.image1.canvas.pixels[round(Jj* Form1.Image1.ClientWidth/10000),round(170-TS_t*140)]:=0; {}
  form1.image1.canvas.pixels[round(Jj* Form1.Image1.ClientWidth/10000),round(170-RhoPh*10)]:=$0040c0;
                     end;


 {******************************************************}
 {******************************************************}
  {******************************************************}
   {******************************************************}
    {******************************************************}
    {******************************************************}


end;

procedure ShowTR();
var
WL: integer;
st1:string[10];
st2,st3,st4:string[20];
Theta1,Phi1:double;
Theta2,Phi2:double;
t1,t2,t3:double;
begin
 WL:=Form1.TrackBar3.Position;
val(Form1.Edit17.Text,Wmin,code);
val(Form1.Edit18.Text,Wmax,code);
  Wloc:=Wmin+(Wmax-Wmin)*WL/800;

 str(Wloc:16:14,st1);
 Form1.Image1.canvas.Brush.Color:=clWhite;
 Form1.Image1.canvas.rectangle(0, 0, Form1.Image1.ClientWidth,28);
 Form1.Image1.canvas.rectangle(0, Form1.Image1.ClientHeight-28, Form1.Image1.ClientWidth,Form1.Image1.ClientHeight+28);
 Form1.Image1.canvas.Pen.Color:=clblue;
 Form1.Image1.canvas.moveto(WL,0);
 Form1.Image1.canvas.lineto(WL,28);

 Form1.Image1.canvas.moveto(WL,Form1.Image1.ClientHeight-28);
 Form1.Image1.canvas.lineto(WL,Form1.Image1.ClientHeight);

 val(Form1.Edit17.Text,Wmin,code);
 val(Form1.Edit18.Text,Wmax,code);
   Form1.Edit19.Text:=st1;

   omega:=Wloc;
   val(Form1.Edit15.Text,Theta1,code);
   val(Form1.Edit16.Text,Phi1,code);



  Ax_r:=cos(Theta1/180*Pi);Ax_i:=0;
  Ay_r:=sin(Theta1/180*Pi)*cos(Phi1/180*Pi);Ay_i:=sin(Theta1/180*Pi)*sin(Phi1/180*Pi);

     MulM();
    v[1,1]:=Tx_r;v[1,2]:=Tx_i;
    v[2,1]:=0;v[2,2]:=0;
    v[3,1]:=Ty_r;v[3,2]:=Ty_i;
    v[4,1]:=0;v[4,2]:=0;

    TS_t := Tx_r * Tx_r + Tx_i * Tx_i + Ty_r * Ty_r + Ty_i * Ty_i;
    TS_r := Rx_r * Rx_r + Rx_i * Rx_i + Ry_r * Ry_r + Ry_i * Ry_i;
    SuS := TS_t + TS_r;


    str(TS_t:18:5,st4);
    str(TS_r:18:5,st2);
    str(SuS:18:5,st3);

    Form1.Memo1.Lines[0]:='t '+st4;
    Form1.Memo1.Lines[1]:='r '+st2;
    Form1.Memo1.Lines[2]:='t+r '+st3;{}

    t1:=Tx_r*Tx_r+Tx_i*Tx_i;
    t2:=Ty_r*Ty_r+Ty_i*Ty_i;
    t3:=ArcTan(sqrt(t1/(t2+0.000001)));

    str(t3:18:5,st2);
   Form1.Memo1.Lines[3]:='atn'+st2;{}

    str(Tx_r:18:5,st4);
    str(Tx_i:18:5,st2);
   Form1.Memo1.Lines[4]:='tx '+st4+'+i*'+st2;{}

    str(Ty_r:18:5,st4);
    str(Ty_i:18:5,st2);
   Form1.Memo1.Lines[5]:='ty '+st4+'+i*'+st2;{}

    str(Rx_r:18:5,st4);
    str(Rx_i:18:5,st2);
   Form1.Memo1.Lines[6]:='Rx '+st4+'+i*'+st2;{}

    str(Ry_r:18:5,st4);
    str(Ry_i:18:5,st2);
   Form1.Memo1.Lines[7]:='Ry '+st4+'+i*'+st2;{}
    {str(Ld:18:5,st2);
   Form1.Memo1.Lines[6]:='Ld '+st2;{}

end;
procedure print_vec(var Vtr:TVct; NNN:string);
var
st1,st2,st3,st4:string;
Ii,Ij:integer;
begin


writeln(MyFile,NNN);

st3:='';
st4:='';
For Ii:=1 to 4 do begin
    str(Vtr[Ii,1]:10:5,st1);
    str(Vtr[Ii,2]:10:5,st2);
    st3:=st1+' '+st2+'*i' ;
     writeln(MyFile,st3);

                   end;

end;

procedure print_A();
var
Theta1,Phi1:double;
st1,st2,st3,st4:string;
begin
val(Form1.Edit15.Text,Theta1,code);
val(Form1.Edit16.Text,Phi1,code);
Ax_r:=cos(Theta1/180*Pi);
Ax_i:=0;
Ay_r:=sin(Theta1/180*Pi)*cos(Phi1/180*Pi);
Ay_i:=sin(Theta1/180*Pi)*sin(Phi1/180*Pi);

    str(Ax_r:18:5,st1);
    str(Ax_i:18:5,st2);
    str(Ay_r:18:5,st3);
    str(Ay_i:18:5,st4);
    Form1.Memo3.Lines[0]:='Vx'+st1+st2+' *i';
    Form1.Memo3.Lines[1]:='Vy'+st3+st4+' *i';




end;



procedure ShowAmpl();
var
Lobs,stps,dL,Lnach,y,Yx,Yy,Lnyn,xg,Zum,Atemp,y1:double;
Lsl:array[0..16] of double;
Il,nomm,nomm_old,sly,sly_old,Ampl,Im,Ii,Ij:integer;
ar_indx,V_indx:integer; {Isl}
AmpCoor:array[0..810,1..2] of integer;
clr:array[0..810] of integer;
st1,st2,st3,st4,st5:string;
flg_end,flg:boolean;
Vtemp,Vtemp1,Vtemp2:TVct;
Mfin_temp,M_temp,Mfin0,Mfin1,Mfin2: TMtr;
Zn,Zk,Zt,SL_max:integer;
Eo_old,Ho_old,Ee_old,He_old,Lloc,VRloc,RhoPh_p:double;
Amp_R,Amp_I,En_No,En_Ne,En_Nd:double;
Ko,Ke:double;
clr1,clr2:integer;


begin
val(Form1.Edit11.Text,L2,code);
Zum:=form1.TrackBar5.Position;

val(Form1.Edit19.Text,omega,code);


val(Form1.Edit7.Text,L1,code);
val(Form1.Edit11.Text,L2,code);
val(Form1.Edit6.Text,Lo1,code);
val(Form1.Edit13.Text,Ld,code);
val(Form1.Edit12.Text,Nd,code);
 MulM();

{ if (PrnFlg) then writeln(MyFile,'++++++++++++++++++++++++++++Ampl++++++++++++++++++++++++++++');{}

 RhoPh_p:=0;
Lobs:=0;flg:=true;
 Form1.Image2.canvas.Brush.Color:=clWhite;
 Form1.Image2.canvas.rectangle(0, 0, Form1.Image2.ClientWidth,Form1.Image2.ClientHeight);


{ if (PrnFlg) then begin
                  writeln(MyFile,'L1 ',L1);
                  writeln(MyFile,'Ld ',Ld);
                  writeln(MyFile,'L2 ',L2);
                  end;   {}


for Il:=0 to 10 do begin
 if flg then
 case sloy[Il] of
 0: begin flg:=false; SL_max:=Il; end;
 1: begin Lobs := Lobs + L1; Lsl[Il] := Lobs;end;{: Rem Толщина херального слоя *MF{}
 2: begin Lobs := Lobs; Lsl[Il] := Lobs;end;{Rem Переходной слой *MDS{}
 3: begin Lobs := Lobs + Ld; Lsl[Il] := Lobs;end;{ Rem Толщина дефектного слоя{}
 4: begin Lobs := Lobs + L2; Lsl[Il] := Lobs;end;{: Rem Толщина херального слоя *MF{}
 end;
                    end;

stps := 800;
dL := Lobs / stps;
xg := 0;
{^^^^^Определили общую толщину системы и шаг на пиксель^^^^}




Eo_old:=Nv*Nv;Ho_old:=1;Ee_old:=Nv*Nv;He_old:=1;{Начальные (справа) показатели преломления}

Zn:=0;
flg_end:=true;
Il:=0;

 {writeln(MyFile,omega);
 writeln(MyFile,'Ld',Ld);
 print_Vec(V,'Vo'); {}
 ZeroFin();



InitMtx(Nv);

MF:=MFc(L1,Lo1,omega);
MF1:=MFc(L2,Lo1,omega);

ML:=MLDc(Ld,omega,Nd);

flg:=true;
ZeroFin;  {Матрица Mfin делается реальной единичной}
Eo_old:=Nv*Nv;Ho_old:=1;Ee_old:=Nv*Nv;He_old:=1;{Начальные (справа) показатели преломления}


{if PrnFlg then print_matr(MF,'MF');{}
if PrnFlg then print_matr(Mfin,'Begin');{**********************************}


for Il:=0 to SL_max do begin

 case sloy[Il] of
 0: begin flg:=false;
          GR_MTRX(Nv*Nv,1,Nv*Nv,1,Eo_old,Ho_old,Ee_old,He_old);
{           if (PrnFlg) then begin
                            writeln(MyFile,'G0');
                            print_matr(GrTmp,'Gr_tmp0');
                          end;{}

          Mfin:=MMc(GrTmp,Mfin);
{          if (PrnFlg) then begin
                            writeln(MyFile,0);
                            print_matr(Mfin,'Gr');
                           end;{}


    end;
 1: begin GR_MTRX(epsilon_o,mu_o,epsilon_e,mu_e,Eo_old,Ho_old,Ee_old,He_old);
          Mfin:=MMc(GrTmp,Mfin);
{          if (PrnFlg) then begin
                            writeln(MyFile,1);
                            print_matr(Mfin1,'Gr_mfin1');
                           end;  {}
          Zk:=round(L1/dL+Zn);
          Zk:=Zk;   {}
          for Zt:=Zn to Zk do
              begin
              clr[Zt]:=$FF0000;
              clr1:=$FF0000;
              clr2:=$FFFF00;
              Lloc:=dL*(Zt-Zn) ;
              Mfin_temp:= MFc(Lloc,Lo1,omega);

              M_temp:=MMc(Mfin_temp,Mfin);

              Vtemp:=MVc(M_temp,V);{}

              Amp_r:=(sqr(Vtemp[1,1]+Vtemp[2,1]+Vtemp[3,1]+Vtemp[4,1]));
              Amp_i:=(sqr(Vtemp[1,2]+Vtemp[2,2]+Vtemp[3,2]+Vtemp[4,2]));
              y:=Amp_r+Amp_i;


              En_No:=(sqr(Vtemp[1,1])+sqr(Vtemp[1,2])+sqr(Vtemp[2,1])+sqr(Vtemp[2,2]))*sqr(No);
              En_Ne:=(sqr(Vtemp[3,1])+sqr(Vtemp[3,2])+sqr(Vtemp[4,1])+sqr(Vtemp[4,2]))*sqr(Ne);
              y1:=En_No+En_Ne;

{              VRloc:=sqr(Vtemp[1,1])+sqr(Vtemp[1,2])+sqr(Vtemp[2,1])+sqr(Vtemp[2,2])+sqr(Vtemp[3,1])+sqr(Vtemp[3,2])+sqr(Vtemp[4,1])+sqr(Vtemp[4,2]);{}

             {y:=VRloc{Yx+Yy};

               RhoPh_p:=RhoPh_p+y1*dL;
               form1.image2.canvas.pixels[800-Zt,round(176-Y*20/Zum)]:=clr1;
               form1.image2.canvas.pixels[800-Zt,round(176-Y1*20/Zum)]:=clr2;
             end;
                    Zn:=Zk+1;


          Eo_old:=epsilon_o;
          Ho_old:=mu_o;
          Ee_old:=epsilon_e;
          He_old:=mu_e;

          Mfin:=MMc(MF,Mfin);
{          if (PrnFlg) then print_matr(Mfin,'MFin_pr');  {}


    end;
 2: begin
          case sloy[Il+1] of
          0:begin
            end;
          1:begin
          GR_MTRX(epsilon_o,mu_o,epsilon_e,mu_e,Eo_old,Ho_old,Ee_old,He_old);
          Mfin:=MMc(GrTmp,Mfin);
          Eo_old:=epsilon_o;
          Ho_old:=mu_o;
          Ee_old:=epsilon_e;
          He_old:=mu_e;
            end;

          2:begin
            end;

          3:begin
          GR_MTRX(Nd*Nd,1,Nd*Nd,1,Eo_old,Ho_old,Ee_old,He_old);
          Mfin:=MMc(GrTmp,Mfin);
          Eo_old:=Nd*Nd;
          Ho_old:=1;
          Ee_old:=Nd*Nd;
          He_old:=1;
            end;


          4:begin
          GR_MTRX(epsilon_o,mu_o,epsilon_e,mu_e,Eo_old,Ho_old,Ee_old,He_old);
          Mfin:=MMc(GrTmp,Mfin);
          Eo_old:=epsilon_o;
          Ho_old:=mu_o;
          Ee_old:=epsilon_e;
          He_old:=mu_e;
            end;

         end;{Case}


          Mfin:=MMc(MDS,Mfin);
{          if (PrnFlg) then print_matr(Mfin,'Povorot');    {}

    end;
 3: begin GR_MTRX(Nd*Nd,1,Nd*Nd,1,Eo_old,Ho_old,Ee_old,He_old);
          Mfin:=MMc(GrTmp,Mfin);
          Zk:=round(Ld/dL+Zn);

          for Zt:=Zn to Zk do
              begin
              clr[Zt]:=$0000FF;
              clr1:=$0000ff;
              clr2:=$FF00ff;

              Lloc:=dL*(Zt-Zn) ;
              Mfin_temp:= MLDc(Lloc,omega,Nd);
              Vtemp1:=V;
              M_temp:=MMc(Mfin_temp,Mfin);
              Vtemp:=MVc(M_temp,Vtemp1);

              Amp_r:=(sqr(Vtemp[1,1]+Vtemp[2,1]+Vtemp[3,1]+Vtemp[4,1]));
              Amp_i:=(sqr(Vtemp[1,2]+Vtemp[2,2]+Vtemp[3,2]+Vtemp[4,2]));

              En_No:=(sqr(Vtemp[1,1])+sqr(Vtemp[1,2])+sqr(Vtemp[2,1])+sqr(Vtemp[2,2]))*sqr(Nd);
              En_Ne:=(sqr(Vtemp[3,1])+sqr(Vtemp[3,2])+sqr(Vtemp[4,1])+sqr(Vtemp[4,2]))*sqr(Nd);
              y1:=En_No+En_Ne;


              VRloc:=sqr(Vtemp[1,1])+sqr(Vtemp[1,2])+sqr(Vtemp[2,1])+sqr(Vtemp[2,2])+sqr(Vtemp[3,1])+sqr(Vtemp[3,2])+sqr(Vtemp[4,1])+sqr(Vtemp[4,2]);


              y:=Amp_r+Amp_i;
              RhoPh_p:=RhoPh_p+y1*dL;
              form1.image2.canvas.pixels[800-Zt,round(176-Y*20/Zum)]:=clr1;
              form1.image2.canvas.pixels[800-Zt,round(176-Y1*20/Zum)]:=clr2;
              end;
          Zn:=Zk+1;

          Eo_old:=Nd*Nd;
          Ho_old:=1;
          Ee_old:=Nd*Nd;
          He_old:=1;
          Mfin:=MMc(ML,Mfin);

    end;


4: begin GR_MTRX(epsilon_o,mu_o,epsilon_e,mu_e,Eo_old,Ho_old,Ee_old,He_old);
          Mfin:=MMc(GrTmp,Mfin);

          Zk:=round(L2/dL+Zn);
          for Zt:=Zn to Zk do
              begin
              clr[Zt]:=$FF00ff;
              clr1:=$FF00ff;
              clr2:=$00FF00;


              Lloc:=dL*(Zt-Zn) ;
              Mfin_temp:= MFc(Lloc,Lo1,omega);

              M_temp:=MMc(Mfin_temp,Mfin);

              Vtemp:=MVc(M_temp,V);{}
              Amp_r:=(sqr(Vtemp[1,1]+Vtemp[2,1]+Vtemp[3,1]+Vtemp[4,1]));
              Amp_i:=(sqr(Vtemp[1,2]+Vtemp[2,2]+Vtemp[3,2]+Vtemp[4,2]));
              y:=Amp_r+Amp_i;

              En_No:=(sqr(Vtemp[1,1])+sqr(Vtemp[1,2])+sqr(Vtemp[2,1])+sqr(Vtemp[2,2]))*sqr(No);
              En_Ne:=(sqr(Vtemp[3,1])+sqr(Vtemp[3,2])+sqr(Vtemp[4,1])+sqr(Vtemp[4,2]))*sqr(Ne);
              y1:=En_No+En_Ne;



{              VRloc:=sqr(Vtemp[1,1])+sqr(Vtemp[1,2])+sqr(Vtemp[2,1])+sqr(Vtemp[2,2])+sqr(Vtemp[3,1])+sqr(Vtemp[3,2])+sqr(Vtemp[4,1])+sqr(Vtemp[4,2]);
{              y:=VRloc;}
               y:=Amp_r+Amp_i;
               RhoPh_p:=RhoPh_p+y1*dL;
               form1.image2.canvas.pixels[800-Zt,round(176-Y*20/Zum)]:=clr1;
               form1.image2.canvas.pixels[800-Zt,round(176-Y1*20/Zum)]:=clr2;
             end;
          Zn:=Zk+1;
          Eo_old:=epsilon_o;
          Ho_old:=mu_o;
          Ee_old:=epsilon_e;
          He_old:=mu_e;
          Mfin:=MMc(MF1,Mfin);

   end;
 end;



end;



   str(RhoPh:18:5,st3);
   Form1.Memo1.Lines[8]:='RhoPh_Teor'+st3;{}
    str((RhoPh_p/Lobs):18:5,st3);
   Form1.Memo1.Lines[9]:='RhoPh_prac'+st3;{}

end;


procedure sloyfill();
var
Ii,Sl:integer;
st:string[40];
begin
for Ii:=0 to 10 do begin
           st:=form1.Memo2.lines[Ii];
           val(st,sloy[Ii],code);
                       end;


end;


procedure TForm1.BitBtn1Click(Sender: TObject);
var
Ii,Ij,Ik: integer;
st1,st2,st3,st4:string[40];
begin
    InitPar();

    sloyfill();
   MainCalc();
   ShowTR();
   ShowAmpl;



end;






procedure TForm1.TrackBar1Change(Sender: TObject);
var
Theta1,Phi1: integer;
st1:string[6];
begin
 Theta1:=Form1.TrackBar1.Position;
 str(Theta1:6,st1);
 Form1.Edit15.Text:=st1;
 print_A();
end;

procedure TForm1.TrackBar2Change(Sender: TObject);
var
Phi1: integer;
st1:string[6];
begin
 Phi1:=Form1.TrackBar2.Position;
 str(Phi1:6,st1);
 Form1.Edit16.Text:=st1;
 print_A();
end;





procedure TForm1.TrackBar3Change(Sender: TObject);
begin
InitPar();
ShowTR();
showAmpl();

end;

procedure TForm1.TrackBar4Change(Sender: TObject);
var
Phi1: integer;
st1:string[6];
begin
 Phi1:=Form1.TrackBar4.Position;
 D_D:=Phi1/180*Pi;
 str(Phi1:6,st1);
 Form1.Edit20.Text:=st1;
  MainCalc();
  InitPar();
ShowTR();
 ShowAmpl();
  
end;



procedure TForm1.Edit2Change(Sender: TObject);
var
code:integer;
Eps: double;
st1:string[6];
begin
{val(Form1.Edit2.Text,No,code);
val(Form1.Edit21.Text,mu_o,code);
epsilon_o:=sqr(No)/mu_o;
 str(epsilon_o:1:6,st1);
 Form1.Edit4.Text:=st1;{}
end;

procedure TForm1.Edit3Change(Sender: TObject);
var
code:integer;
Eps: double;
st1:string[6];
begin
{val(Form1.Edit2.Text,No,code);
val(Form1.Edit21.Text,mu_o,code);
val(Form1.Edit4.Text,epsilon_o,code);
val(Form1.Edit5.Text,rho_E,code);
val(Form1.Edit22.Text,rho_H,code);

val(Form1.Edit3.Text,Ne,code);
mu_e:=mu_o*sqr(rho_H);


epsilon_e:=sqr(Ne)/mu_e;
rho_E:=sqrt(epsilon_e/epsilon_o);
 str(rho_E:1:6,st1);
 Form1.Edit5.Text:=st1;{}
end;

procedure TForm1.Edit4Change(Sender: TObject);
var
code:integer;
Eps: double;
st1:string[6];
begin
val(Form1.Edit4.Text,epsilon_o,code);
val(Form1.Edit5.Text,epsilon_E,code);
val(Form1.Edit21.Text,mu_o,code);
val(Form1.Edit22.Text,mu_e,code);


No:=sqrt(mu_o*epsilon_o);
 str(No:1:6,st1);
 Form1.Edit2.Text:=st1;
Ne:=sqrt(mu_e*epsilon_e);
 str(Ne:1:6,st1);
 Form1.Edit3.Text:=st1;
end;

procedure TForm1.Edit5Change(Sender: TObject);
var
code:integer;
Eps: double;
st1:string[6];
begin

val(Form1.Edit4.Text,epsilon_o,code);
val(Form1.Edit5.Text,epsilon_E,code);
val(Form1.Edit21.Text,mu_o,code);
val(Form1.Edit22.Text,mu_e,code);

Ne:=sqrt(mu_e*epsilon_e);
 str(Ne:1:6,st1);
 Form1.Edit3.Text:=st1;
end;


procedure TForm1.Edit22Change(Sender: TObject);
var
code:integer;
Eps: double;
st1:string[6];
begin

val(Form1.Edit4.Text,epsilon_o,code);
val(Form1.Edit5.Text,epsilon_E,code);
val(Form1.Edit21.Text,mu_o,code);
val(Form1.Edit22.Text,mu_e,code);

Ne:=sqrt(mu_e*epsilon_e);
 str(Ne:1:6,st1);
 Form1.Edit3.Text:=st1;
end;

procedure TForm1.Edit21Change(Sender: TObject);
var
code:integer;
Eps: double;
st1:string[6];
begin
val(Form1.Edit4.Text,epsilon_o,code);
val(Form1.Edit5.Text,epsilon_E,code);
val(Form1.Edit21.Text,mu_o,code);
val(Form1.Edit22.Text,mu_E,code);


No:=sqrt(mu_o*epsilon_o);
 str(No:1:6,st1);
 Form1.Edit2.Text:=st1;
Ne:=sqrt(mu_e*epsilon_e);
 str(Ne:1:6,st1);
 Form1.Edit3.Text:=st1;
end;

procedure TForm1.Button1Click(Sender: TObject);
var
Ii,Ij:integer;
st1,st2,st3,st4:string;
begin

PrnFlg:=true;
ShowAmpl();
{MulM;
{For Ii:= 1 To 4 do begin
   st2:='';
   st4:='|';
    For Ij := 1 To 4 do begin

        str((MF1[Ii, Ij,1]-MF[Ii, Ij,1]):8:5,st1);
        str((MF1[Ii, Ij,2]-MF[Ii, Ij,2]):8:5,st3);

        st2:=st2+st1+'+i*'+st3+', ';

                        end;
                        Form1.Memo1.Lines[Ii-1]:=st2;
                       end;
      str(Ld:18:5,st2);
   Form1.Memo1.Lines[6]:='Ld '+st2;
      {}
PrnFlg:=false;
end;
       {}


procedure TForm1.Button2Click(Sender: TObject);
begin
PrnFlg:=true;
InitPar();
ShowTR();

PrnFlg:=false;
end;

procedure TForm1.TrackBar5Change(Sender: TObject);
begin

ShowAmpl;
end;

procedure TForm1.Button3Click(Sender: TObject);
var
Ii,Ij:integer;
st1,st2,st3,st4:string[90];
begin
For Ii:= 1 To 4 do begin
   st2:='';
   st4:='|';
    For Ij := 1 To 4 do begin
        str(GR_P[Ii,Ij,1]:8:5,st1);
        str(GR_P[Ii,Ij,2]:8:5,st3);
{        str(Mfin_r[Ii, Ij]:8:5,st1);
        str(Mfin_i[Ii, Ij]:8:5,st3);{}



        st2:=st2+st1+'+i*'+st3+', ';

                        end;
                        Form1.Memo1.Lines[Ii-1]:=st2;
                       end;
      str(Nv:18:5,st2);
   Form1.Memo1.Lines[6]:='Nv '+st2;

end;
procedure TForm1.Button4Click(Sender: TObject);
var
Ii,Ij:integer;
st1,st2,st3,st4:string;
begin
writeln(MyFile,'Ax_r',Ax_r,' Ax_i ',Ax_i);
writeln(MyFile,'Ay_r',Ay_r,' Ay_i ',Ay_i);




                        writeln(MyFile,'GR_P');
For Ii:= 1 To 4 do begin
   st2:='';
   st4:='|';
    For Ij := 1 To 4 do begin
        str(GR_P[Ii,Ij,1]:8:5,st1);
        str(GR_P[Ii,Ij,2]:8:5,st3);




        st2:=st2+st1+'+i*'+st3+', ';

                        end;
                        writeln(MyFile,st2);
                       end;

                        writeln(MyFile,'MF');
For Ii:= 1 To 4 do begin
   st2:='';
   st4:='|';
    For Ij := 1 To 4 do begin
        str(MF[Ii,Ij,1]:18:15,st1);
        str(MF[Ii,Ij,2]:18:15,st3);
        st2:=st2+st1+'+i*'+st3+', ';

                        end;
                        writeln(MyFile,st2);
                       end;

                        writeln(MyFile,'GR_L');
For Ii:= 1 To 4 do begin
   st2:='';
   st4:='|';
    For Ij := 1 To 4 do begin
        str(GR_L[Ii, Ij,1]:8:5,st1);
        str(GR_L[Ii, Ij,2]:8:5,st3);
        st2:=st2+st1+'+i*'+st3+', ';

                        end;
                        writeln(MyFile,st2);
                       end;



print_Matr(GL_Ch_I,'GL_Ch_I');
print_Matr(ML,'MLDc');
end;

procedure TForm1.Edit1Change(Sender: TObject);


begin
val(Form1.Edit1.Text,Nv,code);
end;

procedure TForm1.TrackBar6Change(Sender: TObject);
var
DL: integer;
D_L,L_2:double;
st1:string[6];
begin
 DL:=Form1.TrackBar6.Position;
 D_L:=0.5+(100-DL)/100;
{  str(DL:6,st1); {}
 str(D_L:6:4,st1); {}
 Form1.Edit23.Text:=st1;
 L_2:=D_L*L1;
 str(L_2:6:4,st1); {}
 Form1.Edit11.Text:=st1;
 MainCalc();
 InitPar();
 ShowTR(); {}
 ShowAmpl();
end;

procedure TForm1.Button5Click(Sender: TObject);
begin
Form1.TrackBar1.Position:=45;
Form1.TrackBar2.Position:=90;
print_A();
end;



begin
AssignFile(myFile, 'Test.txt');
ReWrite(myFile);
PrnFlg:=false;







begin

end;

end.
