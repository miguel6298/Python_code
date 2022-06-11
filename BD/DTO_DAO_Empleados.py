#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  EBDB 2020/2021

  Autor: Miguel Ruiz Ibáñez

  DTO y DAO de la base de datos Empresa
"""

##########################################################
##                                                      ##
## class Empleado                                       ##
##                                                      ##
##########################################################

class Empleado(dict):
    """ DTO de la tabla Empleados """

    # Atributos de la tabla Empleados
    ATRIBUTOS = ( 'idEmpleado', 'nombre', 'apellidos', 'departamento', 
                 'fechaContrato', 'puesto', 'nivelEducación', 'sueldo',
                 'complemento')

    def __init__(self, data):
        # Inicializa los valores del objeto
        for key in self.ATRIBUTOS:
            if key in data:
                self[key] = data[key]
            else:
                self[key] = None
            #endif
        #endfor
    #enddef

    def __getattr__(self, name):
            return self[name]
    #enddef

    def __setattr__(self, name, value):
        self[name] = value
    #enddef
#endclass

##########################################################
##                                                      ##
## class EmpleadoDao                                    ##
##                                                      ##
##########################################################

class EmpleadoDao(object):
    """ Capa de acceso de la tabla Empleados """

    # Insercción
    _INSERT = 
    """
       INSERT INTO Empleados(nombre, apellidos, departamento, 
                             fechaContrato, puesto, nivelEducacion, sueldo, 
                             complemento)
            VALUES (UPPER(%(nombre)s), %(apellidos)s, 
                    %(departamento)s, %(fechaContrato)s, %(puesto)s, 
                    %(nivelEducacion)s, %(sueldo)s, %(complemento)s)
            
    """

    # Selección por Id de empleado
    _FINDBYID = """
       SELECT idEmpleado, nombre, apellidos, departamento, 
              fechaContrato, puesto, nivelEducacion, sueldo, 
              complemento
         FROM Empleados
        WHERE idEmpleado = %(id)s
    """

    # Selección por nombre de empleado
    _FINDBYNAME = 
    """
       SELECT idEmpleado, nombre, apellidos, departamento, 
              fechaContrato, puesto, nivelEducacion, sueldo, 
              complemento
         FROM Empleados
        WHERE UPPER(nombre) = UPPER(%(name)s)
    """

    # Selección por similitud nombre de empleado
    _FINDLIKENAME = 
    """
        SELECT idEmpleado,nombre, apellidos, departamento, 
               fechaContrato, puesto, nivelEducacion, sueldo, 
               complemento
          FROM Empleados
         WHERE UPPER(nombre) LIKE UPPER(%(name)s)
    """

    # Actualización
    _UPDATE = 
    """
        UPDATE Empleados
           SET nombre = UPPER(%(nombre)s)
         WHERE idEmpleado = %(idEmpleado)s
        """

    # Borrado.
    _DELETE = """
        DELETE FROM Empleados
              WHERE idEmpleado = %(id)s
       """

    def __init__(self, dbase):
        self.dbase = dbase
    #enddef

    ## MétodosCRUD

    ## Create
    def save(self, empleado):
        """ Añade departamento en la tabla Empleados """
        self.dbase.query(self._INSERT, empleado)
    #enddef

    ## Read
    def findbyid(self, idd):
        """ Busca el Empleado de código idd """
        result = self.dbase.query(self._FINDBYID, {'id':idd})
        if result:
            return Empleado(result[0])
        #endif
        return None
    #enddef

    def findbyname(self, name):
        """ Busca empleados con nombre name """
        result = []
        for depto in self.dbase.query(self._FINDBYNAME, {'name':name}):
            result.append(Empleado(depto))
        #endfor
        return result
    #enddef

    def findlikename(self, name):
        """ Busca empleados con nombre %name% """
        data = '%' + name + '%'
        result = []
        for depto in self.dbase.query(self._FINDLIKENAME, {'name':data}):
            result.append(Empleado(depto))
        #endfor
        return result
    #enddef

    ## Update
    def update(self, empleado):
        """ Actualiza la fila empleado en la tabla """
        self.dbase.query(self._UPDATE, empleado)
    #enddef

    ## Delete
    def delete(self, idd):
        """ Borra una fila de la tabla """
        self.dbase.query(self._DELETE, {'id':idd})
    #enddef
#endclass


