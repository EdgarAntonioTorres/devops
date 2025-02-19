#copia_archivos.sh

if [ -z "$1" ]; then
	echo "Uso: $0 <nombre_del_archivo>"
	exit 1
fi
cp ./eventos.txt "$1"
echo "Contenido copiado a $1"

echo "Edgar Torres, t02955128, $(date +%F)"
