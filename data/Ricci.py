import pandas as pd
from Data import Data

class Ricci(Data):

    def __init__(self):
        Data.__init__(self)
        self.dataset_name = 'ricci'
        self.sensitive_attrs = ['Race'] 
        self.unprotected_class_names = ['W']
        self.categorical_features = [ 'Position' ]
        self.features_to_keep = [ 'Position', 'Oral', 'Written', 'Race', 'Combine' ]

    def get_sensitive_attributes(self):
        """
        Returns a list of the names of any sensitive / protected attribute(s) that will be used 
        for a fairness analysis and should not be used to train the model.
        """
        return self.sensitive_attrs

    def get_unprotected_class_names(self):
        return self.unprotected_class_names

    def get_categorical_features(self):
        """
        Returns a list of features that should be expanded to one-hot versions for 
        numerical-only algorithms.  This should not include the protected features 
        or the outcome class variable.
        """
        return self.categorical_features

    def get_features_to_keep(self):
        return self.features_to_keep

    def get_dataset_name(self):
        return self.dataset_name

    def data_specific_processing(self, dataframe):
        ## TODO: any dataset sepcific preprocessing - this should include any ordered categorical
        ## replacement by numbers.
        return dataframe
