#_/_/_/_/_/_/_/_/_/_/#
#　　　 徵兵２ 　　　#
#_/_/_/_/_/_/_/_/_/_/#

sub GET_SOL2 {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	if($in{'num'} eq ""){&ERR("徵兵的人數沒有輸入。");}
	if($in{'type'} eq ""){&ERR("徵兵的種類沒有輸入。");}
	if($in{'num'} =~ m/[^0-9]/){&ERR("徵兵人數中含有數字以外的文字。"); }
	&CHARA_MAIN_OPEN;
	&TIME_DATA;

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"10<><>$SOL_TYPE[$in{'type'}]徵兵 ($in{'num'}人)<>$tt<>$in{'type'}<>$in{'num'}<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"10<><>$SOL_TYPE[$in{'type'}]徵兵 ($in{'num'}人)<>$tt<>$in{'type'}<>$in{'num'}<><>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}

			$i++;
		}
	}

	open(OUT,">./charalog/command/$kid.cgi") or &ERR('打不開文件。');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">NO:$no��$SOL_TYPE[$in{'type'}]徵兵 ($in{'num'}人) 輸入。</font></h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="確定"></form></CENTER><center>
EOM

	&FOOTER;

	exit;

}
1;