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

if($MENTE) { &ERR("維護中。請稍後再試。"); }
&DECODE;
&TOP;

#_/_/_/_/_/_/_/_/_/#
#_/    TOP畫面   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	&CHARA_MAIN_OPEN;
	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	if($xking ne ""){
		open(IN,"./charalog/main/$xking\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($kingid,$kingpass,$king_name,$king_chara) = split(/<>/,$E_DATA[0]);
	}
	if($xgunshi ne ""){
		open(IN,"./charalog/main/$xgunshi\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[0],$tpass[0],$tname[0],$tchara[0]) = split(/<>/,$E_DATA[0]);
		$ximg[0] = "<img src=$IMG/$tchara[0].gif>";
	}
	if($xdai ne ""){
		open(IN,"./charalog/main/$xdai\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[1],$tpass[1],$tname[1],$tchara[1]) = split(/<>/,$E_DATA[0]);
		$ximg[1] = "<img src=$IMG/$tchara[1].gif>";
	}
	if($xuma ne ""){
		open(IN,"./charalog/main/$xuma\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[2],$tpass[2],$tname[2],$tchara[2]) = split(/<>/,$E_DATA[0]);
		$ximg[2] = "<img src=$IMG/$tchara[2].gif>";
	}
	if($xgoei ne ""){
		open(IN,"./charalog/main/$xgoei\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[3],$tpass[3],$tname[3],$tchara[3]) = split(/<>/,$E_DATA[0]);
		$ximg[3] = "<img src=$IMG/$tchara[3].gif>";
	}
	if($xyumi ne ""){
		open(IN,"./charalog/main/$xyumi\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[4],$tpass[4],$tname[4],$tchara[4]) = split(/<>/,$E_DATA[0]);
		$ximg[4] = "<img src=$IMG/$tchara[4].gif>";
	}
	if($xhei ne ""){
		open(IN,"./charalog/main/$xhei\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[5],$tpass[5],$tname[5],$tchara[5]) = split(/<>/,$E_DATA[0]);
		$ximg[5] = "<img src=$IMG/$tchara[5].gif>";
	}

	$p=0;
	foreach(@LOG_DATA){
		$log_list .= "<font color=navy>●</font>$LOG_DATA[$p]<BR>";$p++;
	}

	opendir(dirlist,"./charalog/main");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"./charalog/main/$file")){
				&ERR2("打不開文件！");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	$t_list = "<TR><TH>都市</TH><TH>農民</TH><TH>農業</TH><TH>商業</TH><TH>城</TH><TH>民忠</TH><TH>相場</TH><TH>停留武將</TH></TR>";



	$num=0;
	foreach(@CL_DATA){
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if($econ eq $kcon){
			$list[$epos] .= "$ename ";
		}
	}


	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro,$z2nou_max,$z2syo_max,$z2shiro_max,$z2pri,$z2x,$z2y,$z2souba)=split(/<>/);
		if($z2con eq $kcon){
		$t_list .= "<TR><Th>$z2name</Th><TD>$z2num</TD><TD>$z2nou/$z2nou_max</TD><TD>$z2syo/$z2syo_max</TD><TD>$z2shiro/$z2shiro_max</TD><TD>$z2pri</TD><TD>$z2souba</TD><TD>$list[$zc]</TD></TR>";
		}
		$zc++;
	}

	&HEADER;
	print <<"EOM";
<CENTER>
<TABLE WIDTH="100%" height=100% cellpadding="0" cellspacing="0" border=0><tr><td align=center>
<B><font color="#FFFFFF">$xname國家狀態</font></b>�F
<TABLE border=0 cellspacing=1 bgcolor=$TABLE_C>
    <TBODY bgcolor=FFFFFF>
$t_list
</TBODY></TABLE>
<BR>
<TABLE width=50% border=0 cellspacing=2 bgcolor=$ELE_BG[$xele]>
<TBODY bgcolor=$ELE_C[$xele]>
<TR><TH>官職</TH><TH colspan=2>名字</TH></TR>
<TR><TH NOWRAP> - 君主 - </TH><TH width=100%>$king_name</TH><TH><img src=$IMG/$king_chara.gif></th></TR>
<TR><TH NOWRAP> 軍 師 </TH><TH>$tname[0]</TH><TH>$ximg[0]</th></TR>
<TR><TH NOWRAP> 大 將 軍 </TH><TH>$tname[1]</TH><TH>$ximg[1]</th></TR>
<TR><TH NOWRAP> 騎 馬 將 軍 </TH><TH>$tname[2]</TH><TH>$ximg[2]</th></TR>
<TR><TH NOWRAP> 護 衛 將 軍 </TH><TH>$tname[3]</TH><TH>$ximg[3]</th></TR>
<TR><TH NOWRAP> 弓 將 軍 </TH><TH>$tname[4]</TH><TH>$ximg[4]</th></TR>
<TR><TH NOWRAP> 將 軍 </TH><TH>$tname[5]</TH><TH>$ximg[5]</th></TR>
</TBODY></TABLE><br>


<TABLE border=0 cellspacing=1>
    <TBODY>
          <TR>
<TD>
<form action=\"$FILE_STATUS\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=STATUS><input type=submit value=\"返回都市\"></form>
</TD></TR>
</TBODY></TABLE>


</TD></TR>
</TBODY></TABLE>

EOM

	&FOOTER;
	exit;

}

