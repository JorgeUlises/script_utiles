<?php
function decodificar_url($cadena)
	{       
		$cadena=base64_decode(str_pad(strtr($cadena, '-_', '+/'), strlen($cadena) % 4, '=', STR_PAD_RIGHT)); 
		return cadena;
	}

function decodificar($cadena)
	{      
		$cadena=strrev($cadena);
		$cadena=base64_decode($cadena);
		
		return $cadena;
	
	
	}

function hola($cadena){
return mcrypt_decrypt($cadena);

}
echo decodificar("EHMaXsjbOvAF-oXohX5H1m1RYi48qotnlBIyLtAdSus");
echo hola("EHMaXsjbOvAF-oXohX5H1m1RYi48qotnlBIyLtAdSus");
?>
