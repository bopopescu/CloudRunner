import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../'))
from constants import CRConstants

from dynamodb import DynamoDBAgent

class DatabaseAgentFactory(object):
    '''
    Factory implementation which can be used to instantiate concrete database
    agents.
    '''

    databases = {
        CRConstants.INFRA_AWS: DynamoDBAgent,
    }

    def create_agent(self, infrastructure):
        """
        Instantiate a new database agent.

        @param infrastructure:
        A string indicating the type of infrastructure where the DB
         agent is needed.

        @returns:
        A DB agent instance that implements the BaseDBAgent API.

        @raises NameError:
        If the given input string does not map to any known
         agent type.
        """
        if infrastructure in self.databases:
            return self.databases[infrastructure]()
        else:
            raise NameError('Unrecognized infrastructure: ' + infrastructure)
