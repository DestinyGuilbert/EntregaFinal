import sqlite3
import os

def clean_database(db_path):
    """
    Limpia la base de datos SQLite eliminando todos los datos
    pero manteniendo la estructura de las tablas.
    """
    
    # Verificar que el archivo existe
    if not os.path.exists(db_path):
        print(f"Error: El archivo {db_path} no existe.")
        return
    
    # Crear backup antes de limpiar
    backup_path = db_path + '.backup'
    try:
        import shutil
        shutil.copy2(db_path, backup_path)
        print(f"Backup creado en: {backup_path}")
    except Exception as e:
        print(f"Advertencia: No se pudo crear backup: {e}")
    
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("Iniciando limpieza de la base de datos...")
        
        # Deshabilitar foreign keys temporalmente
        cursor.execute("PRAGMA foreign_keys = OFF")
        
        # Lista de tablas a limpiar (en orden para evitar problemas de foreign keys)
        # Primero las tablas dependientes
        dependent_tables = [
            'auth_user_user_permissions',
            'auth_user_groups', 
            'auth_group_permissions',
            'django_admin_log'
        ]
        
        # Luego las tablas principales
        main_tables = [
            'Mensajes_mensaje',
            'Cuentas_profile',
            'blog_like',
            'blog_comentario', 
            'blog_post',
            'AppCoder_avatar',
            'AppCoder_profesor',
            'django_session'
        ]
        
        # Finalmente las tablas base
        base_tables = [
            'auth_user',
            'auth_group'
        ]
        
        all_tables = dependent_tables + main_tables + base_tables
        
        # Limpiar cada tabla
        for table in all_tables:
            try:
                cursor.execute(f'DELETE FROM "{table}"')
                rows_deleted = cursor.rowcount
                print(f"Tabla {table}: {rows_deleted} registros eliminados")
            except sqlite3.Error as e:
                print(f"Error al limpiar tabla {table}: {e}")
        
        # Reiniciar secuencias de autoincremento
        for table in all_tables:
            try:
                cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = ?", (table,))
            except sqlite3.Error as e:
                print(f"Error al reiniciar secuencia para {table}: {e}")
        
        # Reactivar foreign keys
        cursor.execute("PRAGMA foreign_keys = ON")
        
        # Confirmar cambios
        conn.commit()
        
        print("\n=== Verificación de limpieza ===")
        
        # Verificar que las tablas estén vacías
        for table in all_tables:
            try:
                cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
                count = cursor.fetchone()[0]
                print(f"{table}: {count} registros")
            except sqlite3.Error as e:
                print(f"Error al verificar {table}: {e}")
        
        print("\n¡Limpieza completada exitosamente!")
        
    except sqlite3.Error as e:
        print(f"Error de SQLite: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Error general: {e}")
    finally:
        if conn:
            conn.close()

def main():
    """Función principal"""
    
    # Ruta a tu archivo de base de datos
    db_path = "db.sqlite3"
    
    # Pedir confirmación antes de proceder
    print("ADVERTENCIA: Esta operación eliminará TODOS los datos de la base de datos.")
    print("Se creará un backup automáticamente.")
    
    confirm = input("¿Estás seguro de que quieres continuar? (si/no): ").lower()
    
    if confirm in ['si', 'sí', 's', 'yes', 'y']:
        clean_database(db_path)
    else:
        print("Operación cancelada.")

if __name__ == "__main__":
    main()