var version="p.21";var _ttprofiles=window._ttprofiles||[];var TTProfilesBase;try{TTProfilesBase=(function(){var dM=version;var F=0;var P="A",O="C",J="E",H="G",C="S",A="T",w="U";var ab=0,aa=1,Y=2,X=3,W=5,U=8,a1=30,cl=100,cT=3600;var cZ="0px",aW="action",cj="age",cG="appendChild",aD="async",bi="block",ba="br",n="CA",cC="cacheBuster",bM="callback",aM="callbackScript",c6="checkJob",b8="cluster",ak="clusters",dc="_conversion",dw="cookie",aU=":",l=",",G="conditional",a0="container",db="count",cu="createElement",cg="currentTemperature",bD="createTextNode",bs="https://",ac="dev",dg="_disableCache",cO="disabled",E="display",di="div",a3=".",c5="domain",cN="",Q="_enableDebug",av="_enableServices",bJ="_enableWeather",c0="=",dD="event",b7="exec",cn="executed",dn="expires",o="f",aL="floor",bx="forecast",r="frameBorder",cK="full",df="function",a4="gender",a2="getAge",du="getCity",cF="getCountry",dJ="getCustomAudience",bc="getEquipment",k="getGender",T="getMatchStrings",aV="getMicrosegments",cM="getOperations",z="getProfiles",cx="getLists",aF="getState",cp="getStatus",dR="getSubjects",cL="getOccurrences",by="getSocialClass",Z="getTeam",ag="getTime",aw="getElementsByTagName",c9="getWeather",c1="hash",c2="height",dl="id",bb="iframe",j="img",cY="income",bm="indexOf",bI="innerHTML",dr="insert",cB="insertBefore",g="inside",dG="interval",bn="item",cQ="js",dL="length",bS="location",dq="join",aC="LS",bd="_match",aH="min",dC="max",L="monitor",bC="na",cc="name",a8="not available",aZ="none",bG="number",am="onlyOneInstance",cR="optout",bh="outerHTML",cP="parentNode",bB="partial",bk="path",cD="|",b1="position",af="prod",aj="profiles",bw="prototype",aP="push",dP="?",aA="quantity",b3="random",bV="_registerCallback",ai="replace",a9="required",dQ="_saveProfile",bF="script",bl="scripts",c8=";",dK="_setAccount",M="_setActivationHash",I="setAttribute",aE="_setCA",cb="_setGMT",aB="_setLists",t="_setMode",bH="_setProfile",dA="_setRegion",dB="setTime",bp="_setTTProfile",dN="_setWeather",b0="shift",i="subjects",aY="_sync",bE="/",cq=" ",bN="split",bW="src",b6="style",bO="substr",s="sky",d="t",cd="toLowerCase",bf="ttconversionjs",cA="ttweatherjs",dj="_ttdmp",dh="ttl",az="ttprofilejs",c4="team",dz="text",c="text/javascript",da="toGMTString",dm="Trackyt",be="type",dO="undefined",f="_",cS="unit",an="unitTest",bY="unknown",a="v",B="width",bK="write";var au={"1":"m","2":"f"};var bo={"1":"0-17","2":"18-24","3":"25-34","4":"35-49","5":"50"};var ao="-",cf=document,p=decodeURIComponent,aT=false,y=Math,N=new Date().getTime(),cU=null,dp=true,aR=window,bA=parseInt,c3=setInterval;var m=typeof(console)!="undefined"?console:null;var ad={1:"account value must be set"};var ap,cs,bg=af,u=true,bR="d.t.tailtarget.com",ae="/profile",aN="/weather",b5=".seg.t.tailtarget.com",dy="undef"+b5,cw="/m/",c7="dev-",dk=":8080",dE=dp,cJ=aT;var a7,dt,dv;var cv,ct,bL,ay,at,bj,bZ=[],ce;var ah={};ah[dG]={};ah[db]={};ah[cn]={};function ch(){cm("tailtarget profiles initialization");bP();if(arguments[dL]===aa){for(var dS=ab;dS<arguments[ab][dL];dS++){this.push(arguments[ab][dS])}}a6();cV()}var bP=function(){ch[bw][c9]=bT()};var a6=function(){};ch[bw][a2]="";ch[bw][bc]="";ch[bw][k]="";ch[bw][Z]="";ch[bw][by]="";ch[bw][z]=[];ch[bw][dR]=[];ch[bw][cL]=[];ch[bw][aV]=[];ch[bw][du]="";ch[bw][aF]="";ch[bw][cF]="";ch[bw][cp]=bY;ch[bw][cM]=[];ch[bw][T]=[];ch[bw][cx]=[];ch[bw][dJ]=[];ch[bw][cj]="";ch[bw][a4]="";ch[bw][cY]="";ch[bw][c4]="";ch[bw][aj]=[];ch[bw][i]=[];ch[bw][a]=function(){return dp};ch[bw][aP]=function(){for(var dS=ab;dS<arguments[dL];dS++){var dU=arguments[dS];if(dU[dL]>ab){var dT=dU[b0]();switch(dT){case dc:bQ(dU[b0]());break;case dg:dH();break;case Q:bz(dU[b0]());break;case av:aI(dU[b0]());break;case bJ:ca();break;case bd:dF(dU[b0]());break;case bV:cH(dU[b0]());break;case dQ:ar(dU[b0]());break;case dK:cr(dU[b0]());break;case M:co(dU[b0]());break;case aE:b2(dU[b0]());break;case cb:cE(dU[b0]());break;case aB:aG(dU[b0]());break;case t:b9(dU[b0]());break;case bH:D(dU[b0]());break;case dA:bv(dU[b0]());break;case bp:bU(dU[b0]());break;case dN:cz(dU[b0]());break;case aY:R(dU[b0]());break;default:dx(df+cq+a8,dT)}}}};var b4=function(dS,dT){q(bM,dt,aa);if(de(dt)==df){try{dt(dS,dT)}catch(dU){try{if(m){m.error(dU)}}catch(dV){}}}};var bQ=function(dX){cm(dc);cW(bf);if(de(dX)!==dO){bL=cI(dX);var dV=[];var dU=bL[bN](cD);for(var dW=0;dW<dU[dL];dW++){var dT=dU[dW][bN](aU);var dS={};if(dT[dL]>=Y){dS[dD]=dT[ab];dS[bn]=dT[aa];if(dT[dL]==X){dS[aA]=dT[Y]}else{dS[aA]=aa+cN}dV[aP](dS)}}ch[bw][cM]=dV;q(dc,dX,aa);aK(dc,dX)}cV()};var q=function(dT,dS,dU){if(F>ab&&m){if(de(dU)===dO){dU=aa}if(dU>=F){m.log(dT+aU+cq+dS)}}};var dx=function(dT,dS){if(m){m.error(dT+aU+cq+dS)}};var dH=function(){dE=aT};var bz=function(dS){if(ck(dS)){F=aa}else{if(a5(dS)){F=dS}}q(Q,dS,aa)};var aI=function(){cm(av);q(av,cN,aa);ax();cV()};var ca=function(){cm(bJ);q(bJ,cN,aa);cJ=dp;cV()};var b=function(dS){if(de(dS)!==dO&&de(dS[be])!==dO){var dU;switch(dS[be]){case cQ:if(de(dS[am])!==dO&&dS[am]===dp){var dX=cf[aw](bF);for(var dT=ab;dT<dX[dL];dT++){if(dX[dT][bW]===dS[bW]){q(dS[bW],2);return}}}dU=cf[cu](bF);dU[be]=c;if(de(dS[L])!==dO){ds(dS[L],dS[aM])}break;case j:dU=cf[cu](j);break;case di:dU=cf[cu](di);break;case bb:dU=cf[cu](bb);break;default:}if(de(dS[aD])!==dO&&!u){dU[aD]=dS[aD]}if(de(dS[dl])!==dO){dU[dl]=dS[dl]}if(de(dS[B])!==dO){dU[B]=dS[B]}if(de(dS[c2])!==dO){dU[c2]=dS[c2]}if(de(dS[bW])!==dO){if(de(dS[bW])===df){dU[bW]=dS[bW]()}else{dU[bW]=dS[bW]}}if(de(dS[b6])!==dO){dU[b6]=dS[b6]}if(de(dS[bI])!==dO){var dW=dS[bI];try{dU[cG](cf[bD](dW))}catch(dY){dU[dz]=dW}}if(de(dS[r])!==dO){dU[I](r[cd],ab);dU[r]=dS[r];dU[b6][c2]=cZ;dU[b6][E]=bi}if(dS[be]===cQ&&u){cf[bK](dU[bh])}else{if(dS[be]!=j){if(de(dS[b1])===dO){var dV=cf[aw](bF)[ab];dV[cP][cB](dU,dV)}else{if(dS[b1]==g&&de(dS[a0])!==dO){dS[a0][cG](dU)}}}}aK(dU);return dU}};var cH=function(dS){q(bV,dS,aa);if(!ck(dS)){dt=dS}};var ar=function(dS){q(dQ,dS,aa);if(!ck(dS)){if(!dS[cc]){dS[cc]=dj}if(!dS[dh]||!a5(dS[dh])){dS[dh]=cT}dv=dS}};var cX=function(){var dS=[];if(!ck(ct)){dS[aP](aQ(ct))}if(!ck(cv)){dS[aP](aC+aU+aQ(cv))}if(!ck(ce)){dS[aP](n+aU+aS(ce))}if(dS[dL]){K(dv[cc],dS[dq](cD),dv[dh]*1000,true,dv[c5])}};var cI=function(dS){var dT=p(dS)[ai](/["']/g,cN);return dT};var aQ=function(dS){return dS[ai](/\.\d+/g,cN)[ai](/[^a-z0-9:,\|]/ig,"")};var aS=function(dS){return dS[ai](/[^a-z0-9:,_]/ig,"")};var cr=function(dS){q(dK,dS,aa);if(!ck(dS)){ap=dS;dy=ap[cd]()+b5}};var co=function(dS){q(M,dS,aa);if(!ck(dS)){cs=dS}};var b2=function(dU){q(aE,dU,aa);if(!ck(dU)){dU=cI(dU);dU=aS(dU);var dT=dU[bN](f);if(dT[dL]!=2){return}ce=dT[ab];var dS=ce[bN](l);ch[bw][dJ]=dS}};var cE=function(dS){q(cb,dS,aa);if(!ck(dS)&&!isNaN(bA(dS))){at=bA(dS)}};var aG=function(dU){q(aB,dU,aa);if(ck(dU)){return}var dZ=cI(dU)[bN](f);if(dZ[dL]!=2){return}bj=cI(dU);var dT=[];var dS=bA(dZ[ab]);var dY=dZ[aa][bN](l);for(var dV=ab;dV<dY[dL];dV++){var dX=dY[dV][bN](aU);if(dX[dL]==2&&!isNaN(dX[aa])){var dW=dS+bA(dX[aa]);if(dW>at){dT[aP](dX[ab])}}}ch[bw][cx]=dT};var b9=function(dS){q(t,dS,aa);if(!ck(dS)){bg=dS;if(bg==ac){bR=c7+bR+dk}}};var D=function(dS){cm(bp);cW(az);if(de(dS)!==dO){dS=cI(dS);q(bH,dS,aa);aK(ak,dS);cy(dS)}cV()};var bv=function(dS){if(de(dS)!==dO&&dS===ba){bR=ba+ao+bR}};var bU=function(dS){cm(bp);if(de(dS)!==dO){dS=cI(dS);q(bH,dS,aa);aK(aj,dS);a7=dS;br(dS)}cV()};var cz=function(dS){cm(dN);cW(cA);if(de(dS)!==dO){aK(dN,dS);ay=cI(dS);ch[bw][c9]=bT(ay)}cV()};var bT=function(dY){var dT={};dT[cg]=bC;dT[bx]=[];if(de(dY)===dO){return dT}var dX=dY[bN](f);if(dX[dL]<X){return dT}dT[cg]=bA(dX[ab]);dT[s]=dX[aa];dT[cS]=O;var dS=dX[Y][bN](aU);for(var dV=ab;dV<dS[dL];dV++){var dU=dS[dV][bN](l);if(dU[dL]!==3){break}var dW={};dW[aH]=bA(dU[ab]);dW[dC]=bA(dU[aa]);dW[s]=dU[Y];dT[bx][aP](dW)}return dT};var R=function(dS){if(de(dS)!==dO){if(dS){u=dp}else{u=aT}}else{u=dp}q(aY,u,aa)};var de=function(dS){return typeof(dS)};var cy=function(dT){cv=dT;var dV=bX(b8);if(de(dV)!==dO&&dV!==cU&&dV[dL]>ab){dT=dV}dT=dT[ai](/[^0-9,]/g,cN);if(dT==cR||dT==cO){ch[bw][cp]=dT;return}var dS=dT[bN](l);if(dS[dL]===1&&dS[0]===cN){dS[0]=bC}else{ch[bw][cp]=cK}try{delete _ttprofiles[aj]}catch(dU){}ch[bw][z]=dS;ch[bw][aj]=dS};var br=function(dV){q(bp,dV,aa);if(de(dV)!==dO){if(dV==cR||dV==cO){ch[bw][cp]=dV;return}var dS=dV[bN](f);if(de(dS)!==dO){if(de(dS[ab])!==dO){ct=dS[ab];ch[bw][cp]=aZ;var d9=aT;var dW,dX,dY,ef,d5,eh,d0,ec;var d6=dS[ab][bN](cD);for(var eb=0;eb<d6[dL];eb++){var d7=d6[eb][bN](aU);if(d7[dL]===Y){switch(d7[ab]){case P:d9=dp;dW=d7[aa];break;case O:d9=dp;d0=d7[aa];break;case J:d9=dp;dX=d7[aa];break;case H:d9=dp;dY=d7[aa];break;case C:d9=dp;var dT=d7[aa][bN](l);var eg=[];var d4=[];for(var ea=0;ea<dT[dL];ea++){var d3;var ed;var dU=dT[ea][bN](a3);if(dU[dL]>=Y){d3=dU[ab];ed=dU[aa]}else{d3=dT[ea];ed=aa}eg[aP](d3);d4[aP](ed)}ef=eg[dq](l);d5=d4[dq](l);break;case w:d9=dp;var dZ=d7[aa][bN](l);var ee=[];for(var d8=0;d8<dZ[dL];d8++){var d1;var d2=dZ[d8][bN](a3);if(d2[dL]>=Y){d1=d2[ab]}else{d1=dZ[d8]}ee[aP](d1)}ec=ee[dq](l);break;case A:d9=dp;eh=d7[aa];break}}}if(dW==cU){ch[bw][a2]=bC;ch[bw][cj]=bC}else{ch[bw][a2]=dW;ch[bw][cj]=V(bo,dW)}if(dX==cU){ch[bw][bc]=bC}else{ch[bw][bc]=dX}if(dY==cU){ch[bw][k]=bC;ch[bw][a4]=bC}else{ch[bw][k]=dY;ch[bw][a4]=V(au,dY)}if(d0==cU){ch[bw][by]=bC}else{ch[bw][by]=d0}if(ef==cU){ch[bw][dR]=[bC];ch[bw][i]=[bC]}else{ch[bw][dR]=ef[bN](l);ch[bw][i]=ef[bN](l)}if(d5==cU){ch[bw][cL]=[bC]}else{ch[bw][cL]=d5[bN](l)}if(ec==cU){ch[bw][aV]=[bC]}else{ch[bw][aV]=ec[bN](l)}if(eh==cU){ch[bw][Z]=bC;ch[bw][c4]=bC}else{ch[bw][Z]=eh;ch[bw][c4]=eh}if(d9&&ch[bw][cp]!=cK){ch[bw][cp]=bB}}ch[bw][du]=x(dS[aa],bC);ch[bw][aF]=x(dS[Y],bC);ch[bw][cF]=x(dS[X],bC)}}};var x=function(dS,dT){if(de(dS)!==dO){if(dS!=cN){return dS}else{return dT}}else{return cN}};var V=function(dU,dS){try{if(ck(dU)||ck(dS)){return cN}return dU[dS]}catch(dT){return cN}};var dI=function(){var dS=true;if(ck(ap)||ap===cN){dx(dm,dK+cq+a9);dS=false}return dS};var aq=function(){return y[aL](y[b3]()*1000000000)};var a5=function(dS){return de(dS)===bG};var ck=function(dS){return de(dS)===dO};var v=function(dT){try{var dU,dS,dX,dV=cf[dw][bN](c8);for(dU=ab;dU<dV[dL];dU++){dS=dV[dU][bO](ab,dV[dU][bm](c0));dX=dV[dU][bO](dV[dU][bm](c0)+aa);dS=dS[ai](/^\s+|\s+$/g,cN);if(dS==dT){return unescape(dX)}}}catch(dW){}};function bX(dT){var dS=new RegExp("[#&]"+dT+"=([^&]*)")[b7](aR[bS][c1]);return dS&&p(dS[aa][ai](/\+/g," "))}var K=function(dZ,dV,d1,dW,dY){try{if(de(dW)!==dO&&!dW){if(de(v(dZ))!==dO){return}}cm(dw);aK(dZ,dV);var dT,dU;dT=new Date();dT[dB](dT[ag]()+(d1));var dX=[];dX[aP](dZ+c0+dV);dX[aP](dn+c0+dT[da]());dX[aP](bk+c0+bE);if(!ck(dY)){dX[aP](c5+c0+dY)}var dS=dX[dq](c8+cq);cf[dw]=dS;q(dZ+c0+dV+dU);cV()}catch(d0){}};function ci(){if(typeof(ttdebug)!="undefined"&&ttdebug===true){return true}return false}function aK(dS,dT){if(ci()&&m){if(typeof(dT)!="undefined"){m.log(dS+": "+dT)}else{m.log(dS)}}}function S(dS,dT){if(ci()&&m){m.error(dS+": "+dT)}}function cm(dS){if(ci()&&m){m.group("profiles: "+dS)}}function cV(){if(ci()&&m){m.groupEnd()}}var bt=aT;var ax=function(){if(bt){return}bt=dp;aX({scripts:[{conditional:function(){return dp},t:{action:dr,type:cQ,async:dp,id:az,monitor:az,callbackScript:function(){var dS=window._ttprofiles||[];dS.push(["_setTTProfile",undefined]);dS.push(["_setProfile",undefined])},src:function(){var dS=dE?"":dP+cC+c0+aq();if(!ck(ap)){return bs+dy+ae+dS}else{return bs+bR+ae+dS}}},f:{}},{conditional:function(){return !ck(cs)&&cs!=cN},t:{action:dr,type:cQ,async:dp,id:bf,monitor:bf,callbackScript:function(){var dS=window._ttprofiles||[];dS.push(["_match",undefined])},src:function(){return bs+dy+cw+cs}},f:{}},{conditional:function(){return cJ},t:{action:dr,type:cQ,async:dp,id:cA,monitor:cA,callbackScript:function(){var dS=window._ttprofiles||[];dS.push(["_setWeather",""])},src:function(){if(!ck(ap)){return bs+dy+aN}else{return bs+bR+aN}}},f:{}},{action:b7,exec:function(){b4(_ttprofiles)}},{action:b7,exec:function(){if(!ck(dv)){cX()}}}]})};var ds=function(dS,dT){q(bM,dS,aa);ah[dG][dS]=c3(function(){bq(dS,dT)},cl)};var bq=function(dS,dT){if(de(ah[db][dS])===dO){ah[db][dS]=ab}ah[db][dS]++;if(ah[db][dS]>=U||de(ah[cn][dS])!==dO){q(dS+": "+ah.count[dS]*cl+" ms",2);clearInterval(ah[dG][dS]);if(de(ah[cn][dS])===dO){ah[cn][dS]=dp;dT()}}};var dF=function(dS){q(bd,dS,aa);if(!ck(dS)){bZ=dS[bN](l);ch[bw][T]=bZ}};var cW=function(dS){q(cn+cq+bM,dS,aa);ah[cn][dS]=dp};var h=[];var aX=function(dS){if(de(dS)!==dO&&de(dS[bl])!==dO){h=dS[bl];al()}};var al=function(){if(de(h)===dO||de(h[dL])===dO||h[dL]<=ab){return}var dT=h[b0]();var dS;if(de(dT[G])!==dO){if(dT[G]()){dS=dT[d]}else{dS=dT[o]}}else{dS=dT}if(dS[aW]===dr){if(de(dS[L])!==dO){b(dS);if(u){al()}else{aJ(dS[L])}}else{al()}}else{if(dS[aW]===b7){dS[b7]();al()}else{al()}}};var aO;var aJ=function(dS){if(de(dS)!==dO){aO=c3(function(){dd(dS)},cl)}};var dd=function(dS){bu(dS)};var bu=function(dS){if(de(dS)!==dO){if(ah[cn][dS]){clearInterval(aO);aO=dO;al()}}};ch[bw][an]=function(dS){return typeof(dS)};return ch})()}catch(e){ttProfilesBaseE(e)}function ttProfilesBaseE(c){try{var b=document.createElement("img");var d;d=c.toString();if(typeof(c)!="undefined"&&typeof(c.stack)!="undefined"){d=d+" "+c.stack.toString()}b.src="//e.tailtarget.com/e?s=p&v="+version+"&e="+encodeURIComponent(d);if(typeof(console)!="undefined"){console.error(c)}}catch(a){if(typeof(console)!="undefined"){console.error(c)}}}try{if(typeof(_ttprofiles.v)=="undefined"){var _ttsHolder=_ttprofiles||[];window._ttprofiles=new TTProfilesBase(_ttsHolder)}}catch(e){ttProfilesBaseE(e)};