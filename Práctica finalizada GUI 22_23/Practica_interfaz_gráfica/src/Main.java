import vista.Vista;
import controlador.Controlador;
/**
 * La clase principal del programa.
 * Inicia la ejecucion del programa creando una instancia de la vista y el controlador,
 * y luego invoca el metodo iniciarVista() del controlador el cual inicia la vista.
 */
public class Main {
	/**
	 * 
	 * @param args ...
	 */
	public static void main(String[] args) {
		Vista vista = new Vista();
		Controlador controlador = new Controlador(vista);
		controlador.iniciarVista();
	}
}
