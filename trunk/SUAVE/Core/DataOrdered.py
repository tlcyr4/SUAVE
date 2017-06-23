# DataOrdered.py
#
# Created:  Jul 2016, E. Botero
# Modified: Sep 2016, E. Botero

   
# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------  

from collections import OrderedDict

# for enforcing attribute style access names
import string
chars = string.punctuation + string.whitespace
t_table = string.maketrans( chars          + string.uppercase , 
                            '_'*len(chars) + string.lowercase )

from warnings import warn
import numpy as np

# ----------------------------------------------------------------------
#   Property Class
# ----------------------------------------------------------------------   

class Property(object):
    
    def __init__(self,key=None):
        """ SUAVE.Core.DataOrdered.Property.__init__(key = None)
            Initializes with a key.
            
            Inputs:
                key - key to be associated with object
            
        """
        self._key = key
        
    def __get__(self,obj,kls=None):
        """ SUAVE.Core.DataOrdered.Property.__init__(obj, kls = none)
            Finds value for property's key in obj.
            
            Inputs:
                obj - dict with key matching property's key
                
            Outputs:
                this property object or value corresponding to key
        """
        if obj is None: return self
        else          : return dict.__getitem__(obj,self._key)
        
    def __set__(self,obj,val):
        """ SUAVE.Core.DataOrdered.Property.__init__(obj, kls = none)
            Sets value for property's key in obj.
            
            Inputs:
                obj - dict with key matching property's key
                val - value to be set
                
        """
        dict.__setitem__(obj,self._key,val)
        
    def __delete__(self,obj):
        """ SUAVE.Core.DataOrdered.Property.__init__(obj, kls = none)
            Deletes value for property's key from obj.
            
            Inputs:
                obj - dict with key matching property's key

        """
        dict.__delitem__(obj,self._key)

    
# ----------------------------------------------------------------------
#   DataOrdered
# ----------------------------------------------------------------------        

class DataOrdered(OrderedDict):
    """     SUAVE.Core.DataOrdered
            Ordered-dictionary-like data structure with attribute style access.
    """
    
    _root = Property('_root')
    _map  = Property('_map')    
    
    def append(self,value,key=None):
        """ SUAVE.Core.DataOrdered.append(value, key = None)
            Add an entry to the dictionary.
            
            Inputs:
                value - value to be added
                key - key/attribute name for value, uses tag if none given
        """
        if key is None: key = value.tag
        key_in = key
        key = key.translate(t_table)
        if key != key_in: warn("changing appended key '%s' to '%s'\n" % (key_in,key))
        if key is None: key = value.tag
        if key in self: raise KeyError, 'key "%s" already exists' % key
        self[key] = value    

    def __defaults__(self):
        """ SUAVE.Core.DataOrdered.__defaults__()
            No defaults to add.
        """
        pass
    
    def __getitem__(self,k):
        """ SUAVE.Core.DataOrdered.__getattribute__(k)
            Allows dict-style access to values in data object.
            
            Inputs:
                k - the attribute name or key of the item
            
            Outputs:
                attribute or corresponding value in dictionary
            
        """
        if not isinstance(k,int):
            return super(DataOrdered,self).__getattribute__(k)
        else:
            return super(DataOrdered,self).__getattribute__(self.keys()[k])
    
    def __new__(cls,*args,**kwarg):
        """ SUAVE.Core.DataOrdered.__new__(cls,*args,**kwarg)
            Initializes data with all defaults from trunk to leaf of class heirarchy.
            
            Inputs:
                cls - class of data object
                *args - not used
                **kwarg - not used
            
            Outputs:
                self - new instance of data object
                
        """
        # Make the new:
        self = OrderedDict.__new__(cls)
        
        if hasattr(self,'_root'):
            self._root
        else:
            root = [] # sentinel node
            root[:] = [root, root, None]
            dict.__setitem__(self,'_root',root)
            dict.__setitem__(self,'_map' ,{})        
        
        # Use the base init
        self.__init2()
        
        # get base class list
        klasses = self.get_bases()
                
        # fill in defaults trunk to leaf
        for klass in klasses[::-1]:
            klass.__defaults__(self)
            
        return self
    
    def __init__(self,*args,**kwarg):
        """ SUAVE.Core.DataOrdered.__init__()
            Initializes the data object.
            
            Inputs:
                *args - input data to be appended into data object
                **kwarg - input data to be appended into data object
            
        """

        # handle input data (ala class factory)
        input_data = DataOrdered.__base__(*args,**kwarg)
        
        # update this data with inputs
        self.update(input_data)
        
        
    def __init2(self, items=None, **kwds):
        """ SUAVE.Core.DataOrdered.__init__()
            Initializes the data object.
            
            Inputs:
                items - input data to be appended into data object
                **kwds - input data to be appended into data object
            
        """
        def append_value(key,value):               
            self[key] = value            
        
        # a dictionary
        if hasattr(items, 'iterkeys'):
            for key in items.iterkeys():
                append_value(key,items[key])

        elif hasattr(items, 'keys'):
            for key in items.keys():
                append_value(key,items[key])
                
        # items lists
        elif items:
            for key, value in items:
                append_value(key,value)
                
        # key words
        for key, value in kwds.iteritems():
            append_value(key,value)     


    def __iter__(self):
        """ SUAVE.Core.DataOrdered.__init__()
            Generates values from dictionary.
            
            Outputs:
                One value at a time from dictionary
        """
        return self.itervalues()
            
    def __str__(self,indent=''):
        """ SUAVE.Core.DataOrdered.__str__(indent = '')
            String representation of data object composed of the data nametag and contents.
        
            Inputs:
                indent - specifies separation between items
                
            Outputs:
                args - string representation of data object

        """
        new_indent = '  '
        args = ''
        
        # trunk data name
        if not indent:
            args += self.dataname()  + '\n'
        else:
            args += ''
            
        args += self.__str2(indent)
        
        return args
        
    def __repr__(self):
        """ SUAVE.Core.DataOrdered.__repr__()
            Representation of data object
            
            Outputs:
                data nametag
        """
        return self.dataname()
    
    def get_bases(self):
        """ SUAVE.Core.DataOrdered.get_bases()
            Finds all classes in heirarchy up to Data.
            
            Outputs:
                List of classes in hierarchy from leaf to trunk
        """
        klass = self.__class__
        klasses = []
        while klass:
            if issubclass(klass,DataOrdered): 
                klasses.append(klass)
                klass = klass.__base__
            else:
                klass = None
        if not klasses: # empty list
            raise TypeError , 'class %s is not of type DataBunch()' % self.__class__
        return klasses
    
    def typestring(self):
        """ SUAVE.Core.DataOrdered.typestring()
            Builds a string indicating the type of the data object.
            
            Outputs:
                typestring - a string indicating the type of the data
        """
        typestring = str(type(self)).split("'")[1]
        typestring = typestring.split('.')
        if typestring[-1] == typestring[-2]:
            del typestring[-1]
        typestring = '.'.join(typestring) 
        return typestring
    
    def dataname(self):
        """ SUAVE.Core.DataOrdered.dataname()
            Builds a tag describing the data as a data object of its type.
        
            Ouptuts:
                tag describing the data object as a data object of its own type

        """
        return "<data object '" + self.typestring() + "'>"

    def deep_set(self,keys,val):
        """ SUAVE.Core.DataOrdered.deep_set(keys, val)
            Attribute-style access to items down tree of nested data objects.
            
            Inputs:
                keys - attribute names down to value, separated by dots
                val - value to be set
        """
        if isinstance(keys,str):
            keys = keys.split('.')
        
        data = self
         
        if len(keys) > 1:
            for k in keys[:-1]:
                data = data[k]
        
        data[ keys[-1] ] = val
        
        return data

    def deep_get(self,keys):
        """ SUAVE.Core.DataOrdered.deep_set(keys, val)
            Attribute-style access to items down tree of nested data objects.
            
            Inputs:
                keys - attribute names down to value, separated by dots
                val - value to be retrieved
        """
        if isinstance(keys,str):
            keys = keys.split('.')
        
        data = self
         
        if len(keys) > 1:
            for k in keys[:-1]:
                data = data[k]
        
        value = data[ keys[-1] ]
        
        return value   
    
    def update(self,other):
        """ SUAVE.Core.Data.update(other)
            Recursively appends new items from another data object.
            
            Inputs:
                other - another dict-type with items to be appended
                
        """
        if not isinstance(other,dict):
            raise TypeError , 'input is not a dictionary type'
        for k,v in other.iteritems():
            # recurse only if self's value is a Dict()
            if k.startswith('_'):
                continue
        
            try:
                self[k].update(v)
            except:
                self[k] = v
        return 

    def __delattr__(self, key):
        """ SUAVE.Core.DataOrdered.__delattr__(key, value)
            Allows attribute-style deletion of values in data object.
            
            Inputs:
                k - the attribute name or key of the item
            
        """
        OrderedDict.__delattr__(self,key)
        link_prev, link_next, key = self._map.pop(key)
        link_prev[1] = link_next
        link_next[0] = link_prev
        
    def __eq__(self, other):
        """ SUAVE.Core.DataOrdered.__eq__(other)
            Equality based on equality of antries and order (if both are ordered)
            
            Inputs:
                other - object to be compared to self
                
            Outputs:
                boolean value of whether or not objects are equal
        """
        if isinstance(other, (DataOrdered,OrderedDict)):
            return len(self)==len(other) and np.all(self.items() == other.items())
        return dict.__eq__(self, other)
        
    def __len__(self):
        """ SUAVE.Core.DataOrdered.__len__()
            Determines length of data object.
            
            Outputs:
                the number of key-balue pairs in dict
        """
        return self.__dict__.__len__()   

    ###duplicate method?
    def __iter__(self):
        root = self._root
        curr = root[1]
        while curr is not root:
            yield curr[2]
            curr = curr[1]

    def __reduce__(self):
        items = [( k, DataOrdered.__getitem2(self,k) ) for k in DataOrdered.iterkeys(self)]
        inst_dict = vars(self).copy()
        for k in vars(DataOrdered()):
            inst_dict.pop(k, None)
        return (_reconstructor, (self.__class__,items,), inst_dict)
    
    def __setattr__(self, key, value):
        """ SUAVE.Core.DataOrdered.__setattr__(k, v)
            Allows attribute-style access to values in data object.
            
            Inputs:
                key - the attribute name or key of the item
                value - the new value to be set as attribute or value
                
        """
        if not hasattr(self,key) and not hasattr(self.__class__,key):
        #if not self.has_key(key) and not hasattr(self.__class__,key):
            root = dict.__getitem__(self,'_root')
            last = root[0]
            map  = dict.__getitem__(self,'_map')
            last[1] = root[0] = map[key] = [last, root, key]
        OrderedDict.__setattr__(self,key, value)

    def __setitem__(self,k,v):
        """ SUAVE.Core.DataOrdered.__setattr__(k, v)
            Allows dict-style access to values in data object.
            
            Inputs:
                k - the attribute name or key of the item
                v - the new value to be set as attribute or value
                
        """
        self.__setattr__(k,v)
        
    def __str2(self,indent=''):
        """ SUAVE.Core.DataOrdered.__str2(indent = '')
            Recursively generates string representation of all data in structure
            
            Inputs:
                indent - specified separation between items
                
            Outputs:
                args - string representation of all data
        """
        new_indent = '  '
        args = ''
        
        # trunk data name
        if indent: args += '\n'
        
        # print values   
        for key,value in self.iteritems():
            
            # skip 'hidden' items
            if isinstance(key,str) and key.startswith('_'):
                continue
            
            # recurse into other dict types
            if isinstance(value,OrderedDict):
                if not value:
                    val = '\n'
                else:
                    try:
                        val = value.__str__(indent+new_indent)
                    except RuntimeError: # recursion limit
                        val = ''
                        
            # everything else
            else:
                val = str(value) + '\n'
                
            # this key-value, indented
            args+= indent + str(key) + ' : ' + val
            
        return args     

    def clear(self):
        """ SUAVE.Core.DataOrdered.clear()
            Clear the dictionary.
        """
        try:
            for node in self._map.itervalues():
                del node[:]
            root = self._root
            root[:] = [root, root, None]
            self._map.clear()
        except AttributeError:
            pass
        self.__dict__.clear()
        
    def get(self,k,d=None):
        """ SUAVE.Core.DataOrdered.get(k, d = None)
            Return the value for a given key.
            
            Inputs:
                k - key associated with desired value
                d - default to be returned if key is not in dict
        """
        return self.__dict__.get(k,d)
        
    def has_key(self,k):
        """ SUAVE.Core.DataOrdered.has_key()
            Check to see if the key appears in the dictionary.
            
            Inputs:
                k - key to be checked
                
            Outputs:
                boolean value for whether or not key is in dict
        """
        return self.__dict__.has_key(k)

    # allow override of iterators
    __iter = __iter__
    __getitem2 = OrderedDict.__getattribute__ 

    def keys(self):
        """ SUAVE.Core.DataOrdered.keys()
            Return a list of keys in the dictionary
            
            Outputs:
                list of keys in the dictionary
        """
        return list(self.__iter())
    
    def values(self):
        """ SUAVE.Core.DataOrdered.keys()
            Return a list of values in the dictionary
            
            Outputs:
                list of keys in the dictionary
        """
        return [self[key] for key in self.__iter()]
    
    def items(self):
        """ SUAVE.Core.DataOrdered.keys()
            Return a list of tuples of keys and values in the dictionary
            
            Outputs:
                list of keys in the dictionary
        """
        return [(key, self[key]) for key in self.__iter()]
    
    def iterkeys(self):
        """ SUAVE.Core.DataOrdered.iterkeys()
            Generate keys in the dictionary
            
            Outputs:
                One key at a time
        """
        return self.__iter()
    
    def itervalues(self):
        """ SUAVE.Core.DataOrdered.iterkeys()
            Generate values in the dictionary
            
            Outputs:
                One value at a time
        """
        for k in self.__iter():
            yield self[k]
    
    def iteritems(self):
        """ SUAVE.Core.DataOrdered.iterkeys()
            Generate tuples of keys and values in the dictionary
            
            Outputs:
                One tuple of key-value pair at a time
        """
        for k in self.__iter():
            yield (k, self[k])   


# for rebuilding dictionaries with attributes
def _reconstructor(klass,items):
    """ SUAVE.Core.DataOrdered._reconstructor(klass, items)
        Rebuilds a dictionary with attributes.
        
        Inputs:
            klass - desired class for data
            
        Outputs:
            self - instance of DataOrdered
    """
    self = DataOrdered.__new__(klass)
    DataOrdered.__init__(self,items)
    return self
            

# ----------------------------------------------------------------------
#   Module Tests
# ----------------------------------------------------------------------        

if __name__ == '__main__':
    
    d = DataOrdered()
    d.tag = 'data name'
    d['value'] = 132
    d.options = DataOrdered()
    d.options.field = 'of greens'
    d.options.half  = 0.5
    print d
    
    import numpy as np
    ones = np.ones([10,1])
        
    m = DataOrdered()
    m.tag = 'numerical data'
    m.hieght = ones * 1.
    m.rates = DataOrdered()
    m.rates.angle  = ones * 3.14
    m.rates.slope  = ones * 20.
    m.rates.special = 'nope'
    m.value = 1.0
    
    print m
    
    V = m.pack_array('vector')
    M = m.pack_array('array')
    
    print V
    print M
    
    V = V*10
    M = M-10
    
    print m.unpack_array(V)
    print m.unpack_array(M)
    
