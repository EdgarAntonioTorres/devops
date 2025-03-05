#atributos.sh
if [ -z "$1" ]; then
	echo "Uso: $0 <directorio>"
	exit 1
fi

output="atributosl.txt"
echo "Permisos | Usuario | Grupo | Tamaño en bytes | Fecha y Hora | Nombre del Archivo" > "$output"
ls -lh "$1" | awk '{print $1, "|", $3, "|", $4, "|", $5, "|", $6, $7, $8, "|", $9}' >> "$output"
echo "Lista de atributos guardada en $output"

echo "Edgar Torres, t02955128, $(date +%F)"
