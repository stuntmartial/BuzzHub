# from celery import decorators
from celery.app import shared_task
from .utility import runForwardProp


# Runs Forward Propagation through the DEEPLINKER model
@shared_task
def ForwardPropSchedule():
    runForwardProp()
    return "OK"
