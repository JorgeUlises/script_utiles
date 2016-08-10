#!/usr/bin/php
<?php

/**
 * IMPORTANTE: La frase de seguridad predeterminada debe cambiarse antes instalar el aplicativo. Cambiarla después puede dejar
 * inservible la instalación si esta depende de variables codificadas con la clave anterior 
 * (p.e. si se guardaron datos codificados en la base de datos o en config.inc.php).
 * 
 * 
 * @todo Mejorar la clase para que acepte otras semillas. 
 * 
 */
#require_once ("aes.class.php");
#require_once ("aesctr.class.php");
class Encriptador {
	private static $instance;
	private $llave;
	private $iv;
	//Se requiere una semilla de 16, 24 o 32 caracteres
	const SEMILLA = 'MI_SEMILLA_ENCRI';
	
	// Constructor
	function __construct($llave = '') {
		if ($llave === '') {
			// Llave predeterminada
			$this->llave = self::SEMILLA;
		} else {
			$this->llave = $llave;
		}	
	}

	function codificar($cadena) {
		if (function_exists ( 'mcrypt_encrypt' )) {
			$cadena = mcrypt_encrypt ( MCRYPT_RIJNDAEL_256, $this->llave, $cadena, MCRYPT_MODE_ECB ) ;
		} else {
			echo 'Instale el paquete php-mcrypt o php5-mcrypt dependiendo de su distritución'.PHP_EOL;
			exit();
		}
		$cadena=trim($this->base64url_encode($cadena));
		return $cadena;
	}
	
	function decodificar($cadena) {
		$cadena=$this->base64url_decode($cadena);
		if (function_exists ( 'mcrypt_decrypt' )) {
			$cadena =  mcrypt_decrypt ( MCRYPT_RIJNDAEL_256, $this->llave, $cadena , MCRYPT_MODE_ECB ) ;
		} else {
                        echo 'Instale el paquete php-mcrypt o php5-mcrypt dependiendo de su distritución'.PHP_EOL;
                        exit();
		}
		$cadena=trim($cadena);
		return $cadena;
	}
	
	function codificar_url($cadena, $enlace = '') {
		$cadena = $this->codificar ( $cadena );
		return $enlace . "=" . $cadena;
	}
	
	/**
	 *
	 * Método para decodificar la cadena GET para obtener las variables de la petición
	 *
	 * @param
	 *        	$cadena
	 * @return boolean
	 */
	function decodificar_url($cadena) {
		$cadena = $this->decodificar ( $cadena );
		
		parse_str ( $cadena, $matriz );
		
		foreach ( $matriz as $clave => $valor ) {
			$_REQUEST [$clave] = $valor;
		}
		
		return true;
	}
	function codificarClave($cadena) {
		return sha1 ( md5 ( $cadena ) );
	}
	
	function base64url_encode($data) {
		return rtrim(strtr(base64_encode($data), '+/', '-_'), '=');
	}
	
	function base64url_decode($data) {
		return base64_decode(str_pad(strtr($data, '-_', '+/'), strlen($data) % 4, '=', STR_PAD_RIGHT));
	}
}

function leerSTDIN() {
    stream_set_blocking(STDIN, false);//Impide el bloqueo de la terminal
    $stdin = fopen("php://stdin", "r");
    $input = stream_get_contents($stdin);
    var_dump($input);die;
    $lines = explode("\n", $input);

    foreach($lines as $line) {
        echo "$line\n";
    }
}

function non_block_read($fd, &$data) {
    $read = array($fd);
    $write = array();
    $except = array();
    $result = stream_select($read, $write, $except, 0);
    if($result === false) throw new Exception('stream_select failed');
    if($result === 0) return false;
    $data = stream_get_line($fd, 1);
    return true;
}

$semilla = isset($argv[1])?$argv[1]:'';
if($semilla=='-h'||$semilla=='--help'||$semilla==''){
	echo 'php '.$argv[0].' <semilla> <codificar o decodificar>'."\n";
	exit();
}
$enc = new Encriptador($semilla);

$accion = isset($argv[2])?(strtoupper($argv[2][0])=='C')?'codificar':'decodificar':'codificar';

echo 'Inserte lineas a '.$accion.':'.PHP_EOL;

$linea = '';
while(1) {
    $char = '';
    if(non_block_read(STDIN, $char)) {
	$linea .= $char;
    } else {
	if($linea != ''){
		$lineas = explode("\n", $linea);
		echo PHP_EOL;
		foreach ($lineas as $l){
			if($l!=''){
				echo $enc->{$accion}($l).PHP_EOL;
			}
		}
		echo PHP_EOL;
		$linea = '';
	}
    }
}
?>
