#!/usr/bin/perl

#################################################################
#　【免責條款】　　　　　　　　　　　　　　　　　　     　　　　#
#　這個程式是免費軟件。如使用這個程式　　　　　　　　     　　　#
#　而損失者程式作者將不承擔一切之責任。　　　　　　　     　　　#
#　有關設置的問題請到本站的揭示板討論。　　　　　　　　     　　#
#　任何問題不接受郵件查詢。　　　　　　　　　　　　　　     　  #
#################################################################

#require 'jcode.pl';
require './withlove_sgkini/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("程序核對一時停止。"); }
&DECODE;
&TOP;

#_/_/_/_/_/_/_/_/_/#
#_/    TOP畫面   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	$date = time();
	$month_read = "./withlove_sgklog/date_count.cgi";
	open(IN,"$month_read") or &ERR2('打不開文件。');
	@MONTH_DATA = <IN>;
	close(IN);
	&TIME_DATA;

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$S_MES .= "<font color=008800>● </font>$S_MOVE[$p]<BR>";$p++;}

	open(IN,"$MAP_LOG_LIST2");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$D_MES .= "<font color=000088>●</font>$S_MOVE[$p]<BR>";$p++;}

	$hit = 0;
	@month_new=();

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	$old_date = sprintf("%02d\年%02d\月", $F_YEAR+$myear, $mmonth);

	if($ACT_LOG){
		$actfile = "./withlove_sgklog/act_log.cgi";
		open(IN,"$actfile");
		@ACT_DATA = <IN>;
		close(IN);
		($qsec,$qmin,$qhour,$qday) = localtime($date);
		$p=0;
		while($p<5){$A_MES .= "<font color=880000>● </font>$ACT_DATA[$p]<BR>";$p++;}

		$ACT_MES = "<TD bgcolor=#EFE0C0 colspan=\"2\" width=80% height=100><font color=#8E4C28 size=2>$A_MES</font></TD>";

	}

	open(IN,"$TOWN_LIST") or &ERR("打不開指定的文件。");
	@TOWN_DATA = <IN>;
	close(IN);
	($zwname,$wzc)=split(/<>/,$TOWN_DATA[0]);
	$zzhit=0;
	foreach(@TOWN_DATA){
		($zwname,$zwcon)=split(/<>/);
			if($wzc ne $zwcon){$zzhit=1;}
			$wzc = $zwcon;
	}


	&CHEACK_COM;
	if($mtime + $TIME_REMAKE < $date){
		if($mtime eq ""){
		$mtime = $date;
		&MAP_LOG("遊戲開始。");
		}else{
		$mtime += $TIME_REMAKE;
		}
		$mmonth++;
		if($mmonth > 12){
			$myear++;
			$mmonth=1;
		}
		unshift(@month_new,"$myear<>$mmonth<>$mtime<>\n");
		if($ACT_LOG){
			($qsec,$qmin,$qhour,$qday) = localtime($mtime);
			unshift(@ACT_DATA,"===============\[$myear年$mmonth月\]=================\n");
		}

		open(IN,"$COUNTRY_LIST") or &ERR2('沒開文件。err no :country');
		@COU_DATA = <IN>;
		close(IN);
		@NEW_COU_DATA=();
		foreach(@COU_DATA){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri)=split(/<>/);
			$xvmark++;
			push(@NEW_COU_DATA,"$xvcid<>$xvname<>$xvele<>$xvmark<>$xvking<>$xvmes<>$xvsub<>$xvpri<>\n");
		}
		open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY 不能寫上數據。');
		print OUT @NEW_COU_DATA;
		close(OUT);

		$b_hit = 0;
		if($mmonth eq "1"){
			&MAP_LOG("$mmonth月：<font color=orange>稅金</font>支付各武將工資。");
			$b_hit = 1;
		}elsif($mmonth eq "7"){
			&MAP_LOG("$mmonth月：<font color=orange>收穫</font>支付各武將米糧。");
			$b_hit = 1;
		}

		$eve_date = sprintf("%02d\年%02d\月", $F_YEAR+$myear, $mmonth);
		$ihit=0;
		if(!int(rand(40))){
			$ihit=1;
			$ino = int(rand(6));
			if($ino eq 0){
				&MAP_LOG("<font color=red>【災害】</font>\[$eve_date\]大群蝗蟲襲擊田地！");
				&MAP_LOG2("<font color=red>【災害】</font>\[$eve_date\]大群蝗蟲襲擊田地！");
			}elsif($ino eq 1){
				&MAP_LOG("<font color=red>【災害】</font>\[$eve_date\]在各地發生了洪水！");
				&MAP_LOG2("<font color=red>【災害】</font>\[$eve_date\]在各地發生了洪水！");
			}elsif($ino eq 2){
				&MAP_LOG("<font color=red>【災害】</font>\[$eve_date\]疫病流行。不少都市的人民也受到感染。。");
				&MAP_LOG2("<font color=red>【災害】</font>\[$eve_date\]疫病流行。不少都市的人民也愛到感染。。");
			}elsif($ino eq 3){
				&MAP_LOG("<font color=red>【豐作】</font>\[$eve_date\]農作物豐收，各地農民舉行慶祝活動。");
				&MAP_LOG2("<font color=red>【豐作】</font>\[$eve_date\]農作物豐收，各地農民舉行慶祝活動。");
			}elsif($ino eq 4){
				&MAP_LOG("<font color=red>【災害】</font>\[$eve_date\]發生了大地震！");
				&MAP_LOG2("<font color=red>【災害】</font>\[$eve_date\]發生了大地震！");
			}elsif($ino eq 5){
				&MAP_LOG("<font color=red>【商旺】</font>\[$eve_date\]各都市的商店興旺熱鬧。");
				&MAP_LOG2("<font color=red>【商旺】</font>\[$eve_date\]各都市的商店興旺熱鬧。");
			}
		}
		if($b_hit){

		# 行情變動
		@NEW_TOWN_DATA=();
		foreach(@TOWN_DATA){
			($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/);
			if(!int(rand(2.0))){
				$zsouba += int(rand(0.5)*100)/100;
				if($zsouba > 1.2){
					$zsouba = 1.2;
				}
			}else{
				$zsouba -= int(rand(0.5)*100)/100;
				if($zsouba < 0.8){
					$zsouba = 0.8;
				}
			}
			if($zpri >= 50){
				$znum_add = int(80 * ($zpri - 50));
				if($znum_add < 500){$znum_add=500;}
				$znum += $znum_add;
				if($znum > $NOU_MAX){$znum=$NOU_MAX;}
			}else{
				$znum -= int(80 * (50 - $zpri));
				if($znum < 0){$znum=0;}
			}
			if($ihit){
				if($ino eq 0){
					$znou = int($znou * 0.8);
				}elsif($ino eq 1){
					$znou = int($znou * 0.9);
					$zsyo = int($zsyo * 0.9);
					$zshiro = int($zshiro * 0.9);
				}elsif($ino eq 2){
					$znum = int($znum * 0.8);
				}elsif($ino eq 3){
					$znou = int($znou * 1.2);
					if($znou > $znou_max){$znou=$znou_max;}
				}elsif($ino eq 4){
					$znou = int($znou * 0.8);
					$zsyo = int($zsyo * 0.8);
					$zshiro = int($zshiro * 0.8);
					$znum = int($znum * 0.9);
				}elsif($ino eq 5){
					$zsyo = int($zsyo * 1.1);
					if($zsyo > $zsyo_max){$zsyo=$zsyo_max;}
					$znum = int($znum * 1.1);
					if($znum > $NOU_MAX){$znum=$NOU_MAX;}
				}
			}

			push(@NEW_TOWN_DATA,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
		}
		open(OUT,">$TOWN_LIST");
		print OUT @NEW_TOWN_DATA;
		close(OUT);
		}
		open(OUT,">$month_read");
		print OUT @month_new;
		close(OUT);

	}
	if($ACT_LOG){
		if(@ACT_DATA > 800) { splice(@ACT_DATA,800); }
		open(OUT,">$actfile");
		print OUT @ACT_DATA;
		close(OUT);
	}

	$MESS1 = "<A href=\"$FILE_CONTNUE\">【繼續遊戲】</a>";
	$MESS2 = "<A href=\"$FILE_ENTRY\">【新規登錄】</a>";
	&roses_counter;
	$new_date = sprintf("%02d\年%02d\月", $F_YEAR+$myear, $mmonth);
	$next_time = int(($mtime + $TIME_REMAKE - $date) / 60);


	&HEADER;
	print <<"EOM";
<!--[<a href=./i-index.cgi>攜帶用</a>]-->
<CENTER>


<TABLE WIDTH="514" height=100% cellpadding="0" cellspacing="0" border=0><tr><td align=center>
<TABLE border=0 width=80% height=100% cellspacing=1>
    <TBODY>
          <TR>
          <TD align=center><p><TABLE height=140><TR><TD align=center><div align="center"><img src="image/title.gif" width="512" height="140"></div><p>
<font size=2 color=#ffffff><p><B>[$new_date]</b><BR>
下次更新<B>$next_time</B> 分<BR></font>
</TD></TR></TABLE>
<p align="center">
<table bgcolor=$TABLE_C align=center border=0>
<form action="$FILE_STATUS" method="POST"><input type="hidden" name="mode" value="STATUS"><TR><TH bgcolor=$TD_C2 height=5>遊戲帳號</TH><td><input type="text" size="10" name="id" value="$_id"></td></TR>
<TR><TH bgcolor=$TD_C2 height=5>帳號密碼</tH><td><input type="password" size="10" name="pass" value="$_pass"></TD></TR>
<TR><td bgcolor=$TD_C1 align=center colspan=2><input type="submit" value="進入"></td></tr></table></form>
            $MESS2 
             
            <A href="$FILE_RANK">【登錄武將一覽】</a> 
             
            <A href="./manual.html">【說明書】</A> 
			
            <a href="./map.cgi" target="blank">【勢力圖】</a> <p>

			<a href="$HOME_URL">【$HOME】</a>
			<a href="$BBS1_URL" target="blank">【$BBS1】</a>
			<a href="$LINK2_URL">【$LINK2】</a>
			<font color="#FFFFFF">最大登錄人數($ENTRY_MAX人)</font><br>

<TABLE width=80% BGCOLOR=$TABLE_C  cellspacing=1><TBODY>$mess</TBODY></TABLE>
<CENTER><HR width="514" size="0"><p align=right>[<font color=8E6C68>TOTAL ACCESS<font color=red><B> $total_count </font></B>HIT</font>]<BR>

</TD>
          </TR>
    <TR><TD>
    <table width="100%" border="0" align="center" cellspacing="0">
          <tr>
            <td><table width="100%" border="1" cellspacing="0" bordercolor="#996600">
                <tr>
                  <TD bgcolor=#EFE0C0 colspan="2" width=100% height="100"><font color=#8E4C28 size=2>$S_MES</font></TD>
                </tr>
                <tr>
                  <TD bgcolor=#EFE0C0 colspan="2" width=100% height="100"><font color=#8E4C28 size=2>$D_MES</font></TD>
                </tr>
               <tr>
                   $ACT_MES
              </tr></table></td>
          </tr>
        </table></TD></TR>       

        </TBODY>
      </TABLE>
</TR></TD></TABLE>

<form method=post action=./admin.cgi>
<font color="#FFFFFF">帳號：</font><input type=text name=id size=7>
<font color="#FFFFFF">密碼：</font><input type=pass name=pass size=7>
<input type=submit value="管理者">
</form>

EOM

	&FOOTER;
	exit;

}

sub roses_counter {

	$file_read = "./withlove_sgklog/counter.cgi";
	open(IN,"$file_read") or &ERR2('打不開文件。');
	@reading = <IN>;
	close(IN);

	($total_count) = split(/<>/,$reading[0]);
	$total_count++;


	open(OUT,">$file_read");
	print OUT "$total_count\n";
	close(OUT);

}

sub CHEACK_COM{

	&D_F_LOCK;
	if (!-e $lockfile2) {&ERR2("文件鎖問題。");}

	open(IN,"$TOWN_LIST");
	@TOWN_DATA = <IN>;
	close(IN);

	open(IN,"$UNIT_LIST") or &ERR("打不開指定的文件。");
	@UNI_DATA = <IN>;
	close(IN);

	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		$town_name[$zc] = "$z2name";
		$town_cou[$zc] = "$z2con";
		$town_get[$z2con] += 1;
		$town_num[$z2con] += $z2num;
		$town_nou[$z2con] += $z2nou;
		$town_syo[$z2con] += $z2syo;
		$zc++;
	}


	$w_lock = 0;
	if($w_lock){
		open(LOCK,"> ./lock/sangoku") or &ERR2("Can't open lockfile: $!");
		flock(LOCK, 2)           or &ERR2("Can't flock        : $!");
	}

	$dir="./charalog/main";
	if($mmonth eq "1" || $mmonth eq "7"){
		opendir(dirlist,"$dir");
		while($file = readdir(dirlist)){
			if($file =~ /\.cgi/i){
				if(!open(page,"$dir/$file")){
					&ERR2("打不開文件！");
				}
				@page = <page>;
				close(page);
				($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex) = split(/<>/,$page[0]);
				$cou_num[$kcon]++;
				$cex_total[$kcon]+=$kcex;
				push(@CL_DATA,"@page<br>");
			}
		}
		closedir(dirlist);
	}

	opendir(dirlist,"$dir");
	$kup_date=0;
	$thit=0;
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("打不開文件！");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/,$page[0]);
			if($kdate + $TIME_REMAKE < $date && $mtime > $kdate){
				$thit=1;
				($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex) = split(/,/,$ksub1);
				if($mmonth eq "1"){
					&SALARY;
					if($cou_num[$kcon] eq "0" || $cou_num[$kcon] eq ""){
						$cou_num[$kcon] = 1;
					}
					$kadd = 0;
					if($cex_total[$kcon] ne 0){
					$kadd  = int(($ksal * $kcex / $cex_total[$kcon]) + $kcex * 1.3);
					}
					$s_num = int($kclass / $LANK);
					if($s_num > 20){$s_num = 20;}
					if($kadd > 1000 + $s_num * 150){$kadd=1000 + $s_num * 150;}
					$kgold += $kadd;
					$k_ex_fol= ($kclass % $LANK)+$kcex;
					$kclass += $kcex;
					if($k_ex_fol > $LANK){
						$s_num = int($kclass / $LANK);
						if($s_num > 20){$s_num = 20;}
						$nadd = int(rand(3));
						if($nadd eq "1"){
							$kstr++;
							$add_m = "武力";
						}elsif($nadd eq "2"){
							$kint++;
							$add_m = "知力";
						}else{
							$klea++;
							$add_m = "統率力";
						}
						$max_sal = 1000 + $s_num * 150;
						&K_LOG("$mmonth月：【<font color=red>$add_m上升一點！</font>】");						&K_LOG("$mmonth月：【<font color=red>$LANK[$s_num]升格！</font>】工資的最大支付額變成<font color=red> $max_sal </font>！");

					}
					$kcex = 0;
					&K_LOG("$mmonth月：稅金徵收了<font color=red>$kadd</font>金。");
				}elsif($mmonth eq "7"){
					&SALARY;
					if($cou_num[$kcon] eq "0" || $cou_num[$kcon] eq ""){
						$cou_num[$kcon] = 1;
					}
					$kadd = 0;
					if($cex_total[$kcon] ne 0){
						$kadd  = int(($ksal * $kcex / $cex_total[$kcon]) + $kcex * 1.3);
					}
					$s_num = int($kclass / $LANK);
					if($s_num > 20){$s_num = 20;}
					if($kadd > 1000 + $s_num * 150){$kadd=1000 + $s_num * 150;}
					$krice += $kadd;
					$k_ex_fol= ($kclass % $LANK)+$kcex;
					$kclass += $kcex;
					if($k_ex_fol > $LANK){
						$s_num = int($kclass / $LANK);
						if($s_num > 20){$s_num = 20;}
						$nadd = int(rand(3));
						if($nadd eq "1"){
							$kstr++;
							$add_m = "武力";
						}elsif($nadd eq "2"){
							$kint++;
							$add_m = "知力";
						}else{
							$klea++;
							$add_m = "統率力";
						}
						$max_sal = 1000 + $s_num * 150;
						&K_LOG("$mmonth月：【<font color=red>$add_m上升一點！</font>】");						&K_LOG("$mmonth月：【<font color=red>$LAMK[$s_num]升格！</font>】工資的最大支付額變成<font color=red> $max_sal </font>！");
					}
					$kcex = 0;
					&K_LOG("$mmonth月：食料收穫得到<font color=red>$kadd</font>。");
				}
				open(IN,"./charalog/command/$kid\.cgi");
				@COM_DATA = <IN>;
				close(IN);
				($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[0]);

				$kdate += $TIME_REMAKE;
				&CHARA_MAIN_INPUT;
				splice(@COM_DATA,0,1);
				push(@COM_DATA,"<><><><><><><>\n");

				open(OUT,">./charalog/command/$kid\.cgi");
				print OUT @COM_DATA;
				close(OUT);

				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/,$TOWN_DATA[$kpos]);
				if($zcon eq "$kcon" || $cid eq "20" || $cid eq "21" || $cid eq "27" || $cid eq "0" || $cid eq ""){

					$kprodmg = 0;
					if($kbook ne "" && $kbook ne 0){
						open(IN,"$PRO_LIST");
						@PRO_DATA = <IN>;
						close(IN);
						($kproname,$kproval,$kprodmg) = split(/<>/,$PRO_DATA[$kbook]);
					}
					if($cid eq "1"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth月：資金不足不能實行。");
						}else{
							$znouadd = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$znou += $znouadd;
							$kgold -= 50;
							if($znou > $znou_max){
								$znou = $znou_max;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth月：$zname的農業開發<font color=red>+$znouadd</font>。");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "2"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth月：資金不足不能實行。");
						}else{
							$zsyoadd = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$zsyo += $zsyoadd;
							$kgold -= 50;
							if($zsyo > $zsyo_max){
								$zsyo = $zsyo_max;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth月：$zname的商業發展<font color=red>+$zsyoadd</font>。");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "3"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth月：資金不足不能實行。");
						}else{
							$zshiroadd = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$zshiro += $zshiroadd;
							$kgold -= 50;
							if($zshiro > $zshiro_max){
								$zshiro = $zshiro_max;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth月：$zname的城牆強化<font color=red>+$zshiroadd</font>。");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "8"){
						$ksub2=0;
						if($krice<50){
							&K_LOG("$mmonth月：米不足不能實行。");
						}else{
							$zpriadd = int($kcha/20 + rand($kcha) / 20);
							$zpri += $zpriadd;
							$krice -= 50;
							if($zpri > 100){
								$zpri = 100;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth月：$zname的民忠<font color=red>+$zpriadd</font>。");
							$kcha_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "10"){
						$ksub2=0;
						if($ksol eq "$klea" && $csub eq $ksub1_ex){
							&K_LOG("$mmonth月：【軍事】：士兵數已達上限。");
						}elsif($kgold < $cnum * $SOL_PRICE[$csub]){
							&K_LOG("$mmonth月：【軍事】：所持金不足。");
						}elsif($znum < $cnum * 10){
							&K_LOG("$mmonth月：【軍事】：農民不足夠。");
						}elsif($zpri < int($cnum / 10)){
							&K_LOG("$mmonth月：【軍事】：農民拒絕。");
						}else{
							if($ksub1_ex eq $csub || $ksub1_ex eq "" && $csub eq 0){
								if($ksol + $cnum > $klea){
									$cnum = $klea - $ksol;
								}
								$ksol += $cnum;
							}else{
								if($cnum > $klea){
									$cnum = $ksol;
								}
								$ksol = $cnum;
							}
							$kgat -= $cnum;
							if($kgat < 0 ){
								$kgat = 0;
							}
							$ksub1_ex = $csub;
							$kcex += 10;
							$kgold -= $cnum * $SOL_PRICE[$csub];
							$znum -= $cnum * 5;
							$zpri -= int($cnum / 10);
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth月：$SOL_TYPE[$ksub1_ex]徵兵<font color=red>$cnum</font>人。");
							$kstr_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "11"){
						$ksub2=0;
						$kgat += int($klea/6 + rand($klea/6));
						if($kgat > 100){
							$kgat = 100;
						}
						$kcex += 15;
						&K_LOG("$mmonth月：士兵的訓練度變成<font color=red>$kgat</font>。");
						$klea_ex++;
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
					}elsif($cid eq "12"){
						$ksub2=0;
						if($ksol eq "0" || $ksol eq ""){
							&K_LOG("$mmonth月：沒有士兵不能守備。");
						}else{
							open(IN,"$DEF_LIST");
							@DEF_LIST = <IN>;
							close(IN);
							my @NEW_DEF_LIST2=();
							$whit=0;
							foreach(@DEF_LIST){
								($tid,$tname,$ttown_id,$ttown_flg,$tcon) = split(/<>/);
								if("$tid" eq "$kid"){
								}else{
									push(@NEW_DEF_LIST2,"$_");
								}
							}
							unshift(@NEW_DEF_LIST2,"$kid<>$kname<>$kpos<>0<>$kcon<>\n");
							open(OUT,">$DEF_LIST");
							print OUT @NEW_DEF_LIST2;
							close(OUT);
							$kcex += 25;
							&K_LOG("$mmonth月：$zname守備。");
							$kcha_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "18"){
						$ksub2=0;
						($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7])=split(/<>/,$TOWN_DATA[$cnum]);
						if($zcon eq $kcon){
							&K_LOG("$mmonth月：不能攻擊自國。");
						}elsif($z[0] ne $kpos && $z[1] ne $kpos && $z[2] ne $kpos && $z[3] ne $kpos && $z[4] ne $kpos && $z[5] ne $kpos && $z[6] ne $kpos && $z[7] ne $kpos ){
							&K_LOG("$mmonth月：$zname沒有鄰接。");
						}else{
							open(IN,"$COUNTRY_LIST");
							@COU_DATA = <IN>;
							close(IN);
							@NEW_COU_DATA=();
							$zvhit=0;
							foreach(@COU_DATA){
								($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri)=split(/<>/);
								if($xvcid eq $zcon){$zvhit=1;last;}
							}
							if($zvhit && $xvmark < 36){
								&K_LOG("$mmonth月：$xvname攻擊。($xvmark回合)");
							}else{
								&COUNTRY_DATA_OPEN("$kcon");
								if($xmark < 36){
									&K_LOG("$mmonth月：$xname攻擊。($xmark回合)");
								}else{
									open(IN,"$DEF_LIST");
									@DEF_LIST3 = <IN>;
									close(IN);
									$d_hit=0;
									foreach(@DEF_LIST3){
										($mdid,$mdname,$mdtown_id,$mdtown_flg,$mdcon) = split(/<>/);
										if($cnum eq $mdtown_id){
											$d_hit=1;last;
										}
									}
									$katt_add2 = 0;
									if("$xdai" eq "$kid"){
										$katt_add2 = 10;
									}elsif("$xuma" eq "$kid"){
										if($ksub1_ex eq "3"){
											$katt_add2 = 10;
										}
									}elsif("$xgoei" eq "$kid"){
										if($ksub1_ex eq "2"){
											$katt_add2 = 10;
										}
									}elsif("$xyumi" eq "$kid"){
										if($ksub1_ex eq "1"){
											$katt_add2 = 10;
										}
									}elsif("$xhei" eq "$kid"){
										if($ksub1_ex eq "0"){
											$katt_add2 = 10;
										}
									}

									$kcex += 20;
									&MAP_LOG("$xname的$kname攻進了$zname。");
									$eid="";
									if($d_hit){
										open(IN,"./charalog/main/$mdid\.cgi");
										@E_DATA = <IN>;
										close(IN);
										($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);
				($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex) = split(/,/,$esub1);
										$last_battle=0;
									}else{
										$ename = "城牆";
										$esol = $zshiro;
										$estr = int($zdef_att/15)+30;
										$egat = 60;
										$last_battle=1;
										$esub1_ex="";
									}

									&K_LOG2("$mmonth月：$xname的$kname攻進了$zname。");
									&E_LOG2("$mmonth月：$xname的$kname與$ename發生戰鬥！");

									&CHARA_ITEM_OPEN;

									if($ksub1_ex eq "1"){
										$katt_add = 10;
										$katt_def = 0;
									}elsif($ksub1_ex eq "2"){
										$katt_add = 0;
										$katt_def = 15;
									}elsif($ksub1_ex eq "3"){
										$katt_add = 20;
										$katt_def = 10;
									}elsif($ksub1_ex eq "4"){
										$katt_add = 40;
										$katt_def = 0;
									}elsif($ksub1_ex eq "5"){
										$katt_add = $kint;
										$katt_def = 0;
									}else{
										$katt_add = 0;
										$katt_def = 0;
									}
									if($esub1_ex eq "1"){
										$eatt_add = 10;
										$eatt_def = 0;
									}elsif($esub1_ex eq "2"){
										$eatt_add = 0;
										$eatt_def = 15;
									}elsif($esub1_ex eq "3"){
										$eatt_add = 20;
										$eatt_def = 10;
									}elsif($esub1_ex eq "4"){
										$eatt_add = 40;
										$eatt_def = 0;
									}elsif($esub1_ex eq "5"){
										$eatt_add = $eint;
										$eatt_def = 0;
									}else{
										$eatt_add = 0;
										$eatt_def = 0;
									}

									$katt = int(($kstr + $karmdmg + $katt_add + $katt_add2 - $eatt_def - int($egat / 2.5))/8);
									if($katt < 0){$katt = 0;}
									$eatt = int(($estr + $earmdmg + $eatt_add - $katt_def - int($kgat / 2.5))/8);
									$kex_add=0;
									$eex_add=0;
									if($eatt < 0){$eatt = 0;}
									$win=0;
									for($count=0;$count<50;$count++){
										$kdmg=0;
										$edmg=0;
										if($ksol <= 0){last;}
										$kdmg = int(rand($katt));
										if($kdmg <= 0){$kdmg=1;}
										$wsol = $esol;
										$esol -= $kdmg;
										
										$kex_add += ($wsol - $esol);
										if($esol <= 0){
											$esol=0;
											&K_LOG2("回合<font color=red>$count</font>：$kname $SOL_TYPE[$ksub1_ex] $ksol人 ↓\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol人 ↓\(-$kdmg\)");
											&E_LOG2("回合<font color=red>$count</font>：$kname $SOL_TYPE[$ksub1_ex] $ksol人 ↓\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol人 ↓\(-$kdmg\)");
											$win = 1;last;
										}

										$edmg = int(rand($eatt));
										if($edmg <= 0){$edmg=1;}
										$wsol = $ksol;
										$ksol -= $edmg;
										$eex_add += ($wsol - $ksol);
										if($ksol <= 0){
											$ksol=0;
											&K_LOG2("回合<font color=red>$count</font>：$kname $SOL_TYPE[$ksub1_ex] $ksol人 ↓\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol人 ↓\(-$kdmg\)");
											&E_LOG2("回合<font color=red>$count</font>：$kname $SOL_TYPE[$ksub1_ex] $ksol人 ↓\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol人 ↓\(-$kdmg\)");
											last;
										}
										&K_LOG2("回合<font color=red>$count</font>：$kname $SOL_TYPE[$ksub1_ex] $ksol人 ↓\(-$edmg\) |$ename $SOL_TYPE[$esub1_ex] $esol人 ↓\(-$kdmg\)");
									}

									$eex_add = int($eex_add/2);
									$kex_add = int($kex_add/2);
									if($win){
										$ksub2_ex++;
										if($last_battle){
											if($town_get[$zcon] <= 1){
												@NEW_COU=();
												foreach(@COU_DATA){
													($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
													if("$zcon" eq "$xcid"){
													}else{
														push(@NEW_COU,"$_");
													}
												}
												open(OUT,">$COUNTRY_LIST");
												print OUT @NEW_COU;
												close(OUT);
												&MAP_LOG2("<font color=red>【滅亡】</font>\[$old_date\]$cou_name[$zcon]滅亡。。");
												&MAP_LOG("<font color=red>【滅亡】</font>\[$old_date\]$cou_name[$zcon]滅亡。。");
											}
												$zcon = $kcon;
												$znou = int($znou*0.8);
												$zsyo = int($zsyo*0.8);
												$znum = int($znum*0.8);
												$zsub1 = int($zsub1*0.8);
												$zdef_att = 0;
												$zpri = int($zpri*0.8);
												$kex_add += 50;
												$kcex += $kex_add;
												$kpos = $cnum;
											@NEW_DEF_LIST3=();
											$pphit=0;
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon) = split(/<>/);
												if("$did" eq "$kid"){
													$pphit=1;
													unshift(@NEW_DEF_LIST3,"$kid<>$kname<>$kpos<>0<>$kcon<>\n");
												}else{
													push(@NEW_DEF_LIST3,"$_");
												}
											}

											if(!$pphit){
												unshift(@NEW_DEF_LIST3,"$kid<>$kname<>$kpos<>0<>$kcon<>\n");
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);

											&K_LOG2("<font color=blue>$zname</font>入手！得到了<font color=red>$kex_add</font>貢獻值！");
											&MAP_LOG2("<font color=blue>【支配】</font>\[$old_date\]$cou_name[$kcon]的$kname支配了$zname。");
											&MAP_LOG("<font color=blue>【支配】</font>\[$old_date\]$cou_name[$kcon]的$kname支配了$zname。");
										}else{
											@NEW_DEF_LIST3=();
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon) = split(/<>/);
												if("$mdid" ne "$did"){
													push(@NEW_DEF_LIST3,"$_");
												}
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);
											$kex_add += 30;
											$kcex += $kex_add;
											$ecex += $eex_add;
											&K_LOG2("$kname擊倒了$ename！得到了<font color=blue>$kex_add</font>貢獻值！");
											&E_LOG2("$ename $kname敗北。。得到了<font color=red>$eex_add</font>貢獻值！");
											&MAP_LOG("<font color=blue>【勝利】</font>$kname擊倒了$ename。");
										}
									}else{
										$eex_add += 30;
										$ecex += $eex_add;
										$kcex += $kex_add;
										&K_LOG2("$kname $ename敗北。。得到了<font color=red>$kex_add</font>貢獻值！");
										&E_LOG2("$ename擊倒$kname！得到了<font color=blue>$eex_add</font>貢獻值！");
									}

									if(!$last_battle){
										if($eid ne ""){
											&ENEMY_INPUT;
										}
									}else{
										$zshiro = $esol;
										$zdef_att -= $kex_add;
										if($zdef_att < 0){
											$zdef_att=0;
										}
										if("$zname" ne ""){
											splice(@TOWN_DATA,$cnum,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");

										}
									}

									$kstr_ex++;
									$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
								}
							}
						}
					}elsif($cid eq "19"){
						$ksub2=0;
						if($csub){
							if($cnum > 3000){
								$cnum = 3000;
							}
							if($cno){
								if($kgold > int($cnum / $csub)){
									$kadd = int($cnum / $csub);
									$kgold -= $kadd;
									$krice += $cnum;
									&K_LOG("$mmonth月：【商人】:支付$kadd金，購買了$cnum米。");
								$kint_ex++;
								$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
								}else{
									&K_LOG("$mmonth月：【商人】：所持金不足。");
								}
							}else{
								if($krice > $cnum * $csub){
									$kadd = int($cnum * $csub);
									$krice -= $kadd;
									$kgold += $cnum;
									&K_LOG("$mmonth月：【商人】：賣出$kadd米，$cnum金增加。");
								$kint_ex++;
								$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
								}else{
									&K_LOG("$mmonth月：【商人】：米不足。");
								}
							}
						}
					}elsif($cid eq "20"){
						$ksub2=0;
						$zhit=0;
						foreach(@z){
							if($_ eq $cnum){
								$zhit=1;
							}
						}
						if($zhit){
							$kpos = $cnum;
							$klea_ex++;
							if($xcid ne "0"){
								$kcex += 20;
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
							&K_LOG("$mmonth月：$town_name[$cnum]移動。");
						}else{
							&K_LOG("$mmonth月：$town_name[$cnum]不能移動。現在位置：$zname");
						}
					}elsif($cid eq "21"){
						$ksub2=0;
						&COUNTRY_DATA_OPEN($kcon);
						if($xcid eq 0){
							if($cou_name[$cnum] eq ""){
								&K_LOG("$mmonth月：那個國家不能仕官。");
							}else{
								if(@B_LIST eq "0"){
									open(IN,"./withlove_sgklog/black_list.cgi");
									@B_LIST = <IN>;
									close(IN);
								}
								$b_hit=0;
								foreach(@B_LIST){
									($bid,$bcon,$bname,$bsub) = split(/<>/);
									if($bid eq $kid && $bcon eq $kcon){
										$b_hit=1;
									}
								}
								if($b_hit){
									&K_LOG("$mmonth月：$cou_name[$cnum]仕官被拒絕了。");
								}else{
									$kcon = $cnum;
									&K_LOG("$mmonth月：$cou_name[$cnum]仕官。");
									&MAP_LOG("$mmonth月：$kname $cou_name[$cnum]仕官。");
								}
							}
						}else{
							&K_LOG("$mmonth月：不能仕官。");
						}
					}elsif($cid eq "22"){
						$ksub2=0;
						open(IN,"$ARM_LIST");
						@ARM_DATA = <IN>;
						close(IN);
						($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/,$ARM_DATA[$cnum]);
						($armname2,$armval2) = split(/<>/,$ARM_DATA[$karm]);
						$armval2 = int($armval2 * 0.6);
						if($armval > $kgold + $armval2){
							&K_LOG("$mmonth月：所持金不足。$armname 金：$armval");
						}else{
							$kgold += $armval2;
							$kgold -= $armval;
							$karm = $cnum;
							&K_LOG("$mmonth月：武器：$armname2<font color=red>$armval2</font>金賣出，$armname購入。");
						}
					}elsif($cid eq "23"){
						$ksub2=0;
						open(IN,"$PRO_LIST");
						@PRO_DATA = <IN>;
						close(IN);
						($proname,$proval,$prodmg,$prowei,$proele,$prosta,$proclass,$protownid) = split(/<>/,$PRO_DATA[$cnum]);
						($proname2,$proval2) = split(/<>/,$PRO_DATA[$kbook]);
						$proval2 = int($proval2 * 0.6);
						if($proval > $kgold + $proval2){
							&K_LOG("$mmonth月：所持金不足。$proname 金：$proval");
						}else{
							$kgold += $proval2;
							$kgold -= $proval;
							$kbook = $cnum;
							&K_LOG("$mmonth月：書籍：$proname購入。");
						}
					}elsif($cid eq "25"){
						$ksub2=0;
						if($kgold < 100){
							&K_LOG("$mmonth月：所持金不足。");
						}else{

							$kgold-=100;
							$kcex += 30;
							open(IN,"$MESSAGE_LIST2");
							@MES_REG2 = <IN>;
							close(IN);
							$mes_num = @MES_REG2;
							if($mes_num > $MES_MAX) { pop(@MES_REG2); }
							unshift(@MES_REG2,"$cnum<>$kid<>$kpos<>$kname<>$csub<>$cno<>$ctime<>$kchara<>$cend<>\n");
							open(OUT,">$MESSAGE_LIST2");
							print OUT @MES_REG2;
							close(OUT);
							&K_LOG("$mmonth月：$cno密書發送。");
							$kcha_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "27"){
						$ksub2=0;
						if($kgold < 50){
							&K_LOG("$mmonth月：所持金不足。");
						}else{
							if($cnum eq "1"){
								$kstr_ex +=2;
								$a_mes = "武力";
							}elsif($cnum eq "2"){
								$kint_ex +=2;
								$a_mes = "知力";
							}else{
								$klea_ex +=2;
								$a_mes = "統率力";
							}
							$kgold-=50;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
							&K_LOG("$mmonth月：$a_mes強化。");
						}
					}elsif($cid eq "28"){
						$ksub2=0;
						$uhit=0;
						foreach(@UNI_DATA){
							($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
							if("$uid" eq "$kid" && $unit_id eq $kid){$uhit=1;last;}
						}
						if(!$uhit){
							&K_LOG("$mmonth月：隊長以外不能實行。");
						}else{

							foreach(@UNI_DATA){
								($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
								if($unit_id eq $kid && $uid ne $unit_id){
									open(IN,"./charalog/main/$uid.cgi");
									@E_DATA = <IN>;
									close(IN);
									($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);								
									$epos = $kpos;
									if($eid ne ""){
										&E_LOG2("$mmonth月：$uunit_name部隊隊長命令$town_name[$kpos]集合。");
										&ENEMY_INPUT;
									}
								}
							}
							$klea_ex++;
							$kcex+=10;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
							&K_LOG("$mmonth月：$uunit_name部隊$town_name[$kpos]集合。");
						}
					}elsif($cid eq "29"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth月：資金不足不能實行。");
						}else{
							$ztecadd = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$zsub1 += $ztecadd;
							$kgold -= 50;
							if($zsub1 > 999){
								$zsub1 = 999;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth月：$zname技術開發：<font color=red>+$ztecadd</font>。");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}elsif($cid eq "30"){
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth月：資金不足不能實行。");
						}else{
							$zdef_att_add = int(($kint+$kprodmg)/12 + rand(($kint+$kprodmg)) / 20);
							$zdef_att += $zdef_att_add;
							$kgold -= 50;
							if($zdef_att > 999){
								$zdef_att = 999;
							}
							$kcex += 30;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>\n");
							}
							&K_LOG("$mmonth月：$zname城牆耐久力強化：<font color=red>+$zdef_att_add</font>。");
							$kint_ex++;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
						}
					}else{
						$ksub2++;
						if($ksub2 > $DEL_TURN){
							unlink("./charalog/main/$kid\.cgi");
							unlink("./charalog/log/$kid\.cgi");
							unlink("./charalog/command/$kid\.cgi");
							&MAP_LOG("[閒置]：$kname帳號刪除。");
							next;
						}
						&K_LOG("$mmonth月：沒有項目實行。");
					}

				}else{
					&K_LOG("$mmonth月：不是本國。");
				}

				$krice -= $ksol;
				if($krice < 0){
					&K_LOG("$mmonth月：<font color=red>【逃脫】</font>：不能支付米予士兵，士兵逃脫！");
					$ksol = 0;
					$krice = 0;
				}

				$uhit=0;
				if($kstr_ex >= 10){
					$kstr++;
					$kstr_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth月：<font color=red>【上升】</font>:$kname的武力１點上升。");
				}
				if($kint_ex >= 10){
					$kint++;
					$kint_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth月：<font color=red>【上升】</font>:$kname的知力１點上升。");
				}
				if($klea_ex >= 10){
					$klea++;
					$klea_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth月：<font color=red>【上升】</font>:$kname的統率力１點上升。");
				}
				if($kcha_ex >= 10){
					$kcha++;
					$kcha_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth月：<font color=red>【上升】</font>:$kname的人望一點上升。");
				}
				if($uhit){
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,";
				}

				&CHARA_MAIN_INPUT;

				if($ACT_LOG){
					($qsec,$qmin,$qhour,$qday) = localtime($kdate);
					unshift(@ACT_DATA,"$kname更新\($qday日 $qhour:$qmin:$qsec\)\n");
				}
				$kup_date++;
				if($kup_date > 10){last;}
			}
		}
	}
	if($thit){
		foreach(@TOWN_DATA){
			$data .= $_;
		}
		&lock("xxx","1") or &ERR2("文件鎖失敗。");
		&data_save("./withlove_sgklog","town_data.cgi","$data");
		&unlock("xxx");
	}

	closedir(dirlist);
	&D_UNLOCK_FILE;
}


#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/      　 LOG的寫入��      _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub E_LOG2 {

	if($eid ne ""){
		open(IN,"./charalog/log/$eid\.cgi");
		@E_LOG2 = <IN>;
		close(IN);
		unshift(@E_LOG2,"$_[0]($mday日$hour時$min分)\n");
		splice(@E_LOG2,20);

		open(OUT,">./charalog/log/$eid\.cgi");
		print OUT @E_LOG2;
		close(OUT);
	}
}

sub K_LOG2 {

	open(IN,"./charalog/log/$kid\.cgi");
	@K_LOG2 = <IN>;
	close(IN);
	unshift(@K_LOG2,"$_[0]($mday日$hour時$min分)\n");
	splice(@K_LOG2,20);
	open(OUT,">./charalog/log/$kid\.cgi");
	print OUT @K_LOG2;
	close(OUT);
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/　　　　 工資計算　 　　　_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub SALARY {

	$ksal=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		if($z2con eq $kcon){
			if($mmonth eq "1"){
				$ksal += int($z2syo * 8 * $z2num / 10000);
			}elsif($mmonth eq "7"){
				$ksal += int($z2nou * 8 * $z2num / 10000);
			}
		}
	}

}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#       FILE LOCK        #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub D_F_LOCK {

	local($retry)=1;
	if (-e $lockfile2) {
		local($mtime) = (stat($lockfile2))[9];
		if ($mtime && $mtime < time - 60) { &D_UNLOCK_FILE; }
	}

	while (!mkdir($lockfile2, 0755)) {
		if (--$retry <= 0) { &ERR2("File lock error!<BR>數據更新中。請稍後再試。");
}
		sleep(1);
	}
}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#     FILE UNLOCK        #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub D_UNLOCK_FILE
{
  rmdir("$lockfile2");
}

sub data_save {
        local($datapath) = $_[0];
		local($file) = $_[1];
		local($data) = "$_[2]";
		local($datafile) = $datapath . '/' . $file;
		local($tmpfile) = $datapath . '/' . $file . '.tmp';
		local($tmp_dummy) = $datapath . '/' . $file . "$$\.tmp";
		local($datadir) = $datapath . '/';
		opendir(DIR, $datadir) ;
		@list = readdir(DIR) ;
		closedir(DIR) ;
		foreach (@list) {
			if ($_ =~ /($file).*\.tmp$/) {
				&ERR2("Temporary File 存在。<br>");
			}
		}
		if(!open(TMP,">$tmpfile")){
			&ERR2("Temporary File 不能作成。<br>");
		}elsif(!close(TMP)){
			&ERR2("Temporary Tile 不能作成。<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("收藏用的暫存文件不能作成。<br>");
		}elsif(!close(DMY)){
			&ERR2("不能使用暫存文件。<br>");
		}elsif(!chmod (0666,"$tmp_dummy")){
			&ERR2("收藏用的暫存文件屬性不能變更。<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("收藏用的暫存文件不能開放。<br>");
		}
		print DMY $data;
		if (!close(DMY)){
			&ERR2("收藏用的暫存文件不能保存。<br>");
		}elsif(!rename("$tmp_dummy" , "$datafile")){
			&ERR2("收藏用的暫存文件更名不能完成。<br>");
		}elsif(!unlink ("$tmpfile")){
			&ERR2("Temporary File 不能刪掉。<br>");
		}
}

sub lock #($file_name, $use_lock)
{
	local($file_name, $use_lock) = @_;
	local($lock_flag) = $file_name . ".lock";

	if ($use_lock) {
	local($i) = 0;
#	return -1 if (!-f $file_name);
	rmdir($lock_flag) if (-d $lock_flag && time - (stat($lock_flag))[9] > 60);
	while(!mkdir($lock_flag, 0755)) {
	select(undef, undef, undef, 0.05);
		return 0 if (++ $i >= 100);
		}
		return 1;
 	}
 	return 1;
}

sub unlock
{
  rmdir("$_[0].lock") if (-d "$_[0].lock");
}

