# This module introduced to analyse the divider 
# including the divide count number
# including the calculated divider number, frequency, period
# including the actual divider number, frequency, period
#  tips: the actual divider include round up and round down number.
# includng the divider error introduced by the divider
# The input include Target frequency, PreDivider, System frequency
#       TargetFrequency: Hz
#       AcqDivider: a interge number between 0 and 15
#       SysFrequency: MHz
#  The Frequency relationship was defined as below:
#       TargetFrequency = SysFrequency / (Divider + 1) / (AcqDivider + 1)
#  The AcqDivider define that the acquisition frequency is "AcqDivider + 1" times
#  of the TargetFrequency.
import math
def DividerAnalyser(TargetFrequency, AcqDivider, SysFrequency):
    Divider_Info = {}
    Second_ns = 1 * math.pow(10,9)
    Second_us = 1 * math.pow(10,6)
# information about the TargetFrequency
    TargetPeriod                            = Second_ns / TargetFrequency
# information about the Acquisition period
    AcquisitionFrequency                    = TargetFrequency * (AcqDivider + 1)
    AcquisitionPeriod                       = Second_ns / AcquisitionFrequency
# information about the system clock
    ClockTime                               = Second_ns / Second_us / SysFrequency
# Round Up Divivder
    DividerUp                               = math.ceil(SysFrequency * Second_us / AcquisitionFrequency) - 1
    Up_AcquisitionFrequency_Actual          = SysFrequency * Second_us / (DividerUp + 1)
    Up_AcquisitionPeriod_Actual             = ClockTime * (DividerUp + 1)
    Up_TargetFrequency_Actual               = SysFrequency * Second_us / (AcqDivider + 1) / (DividerUp + 1)
    Up_TargetPeriod_Actual                  = ClockTime * (AcqDivider + 1) * (DividerUp + 1)
# Round Up Error calculate
    Up_AcquisitionFrequency_Error           = Up_AcquisitionFrequency_Actual - AcquisitionFrequency
    Up_AcquisitionPeriod_Error              = Up_AcquisitionPeriod_Actual - AcquisitionPeriod
    Up_TargetFrequency_Error                = Up_TargetFrequency_Actual - TargetFrequency
    Up_TargetPeriod_Error                   = Up_TargetPeriod_Actual - TargetPeriod
# Round Up Error Relative
    Up_AcquisitionFrequency_RelativeError   = Up_AcquisitionFrequency_Error / AcquisitionFrequency   
    Up_AcquisitionPeriod_RelativeError      = Up_AcquisitionPeriod_Error / AcquisitionPeriod
    Up_TargetFrequency_RelativeError        = Up_TargetFrequency_Error / TargetFrequency
    Up_TargetPeriod_RelativeError           = Up_TargetPeriod_Error / TargetPeriod  
# Round Down Divider
    DividerDown                             = int(SysFrequency * Second_us / AcquisitionFrequency) - 1
    Down_AcquisitionFrequency_Actual        = SysFrequency * Second_us / (DividerDown + 1)
    Down_AcquisitionPeriod_Actual           = ClockTime * (DividerDown + 1)
    Down_TargetFrequency_Actual             = SysFrequency * Second_us / (AcqDivider + 1) / (DividerDown + 1)
    Down_TargetPeriod_Actual                = ClockTime * (AcqDivider + 1) * (DividerDown + 1)
# Round Down Error calculate
    Down_AcquisitionFrequency_Error         = Down_AcquisitionFrequency_Actual - AcquisitionFrequency
    Down_AcquisitionPeriod_Error            = Down_AcquisitionPeriod_Actual - AcquisitionPeriod
    Down_TargetFrequency_Error              = Down_TargetFrequency_Actual - TargetFrequency
    Down_TargetPeriod_Error                 = Down_TargetPeriod_Actual - TargetPeriod
# Round Down Error Relative
    Down_AcquisitionFrequency_RelativeError = Down_AcquisitionFrequency_Error / AcquisitionFrequency   
    Down_AcquisitionPeriod_RelativeError    = Down_AcquisitionPeriod_Error / AcquisitionPeriod
    Down_TargetFrequency_RelativeError      = Down_TargetFrequency_Error / TargetFrequency
    Down_TargetPeriod_RelativeError         = Down_TargetPeriod_Error / TargetPeriod 
# Output DividerInfo
    DividerInfo = {
        "TargetFrequency"                       :   TargetFrequency,
        "TargetPeriod"                          :   TargetPeriod,
        "AcquisitionDivider"                    :   AcqDivider,
        "AcquisitionFrequency"                  :   AcquisitionFrequency,
        "AcquisitionPeriod"                     :   AcquisitionPeriod,
        "SystemClockFrequency"                  :   SysFrequency,
        "SystemClockPeriod"                     :   ClockTime,
    # round Up
        "UpDivider"                             :   DividerUp,
        "UpTargetFrequency"                     :   Up_TargetFrequency_Actual,
        "UpTargetPeriod"                        :   Up_TargetPeriod_Actual,
        "UpAcquisitionFrequency"                :   Up_AcquisitionFrequency_Actual,
        "UpAcquisitionPeriod"                   :   Up_AcquisitionPeriod_Actual,
        "UpTargetFrequencyError"                :   Up_TargetFrequency_Error,
        "UpTargetPeriodError"                   :   Up_TargetPeriod_Error,
        "UpAcquisitionFrequencyError"           :   Up_AcquisitionFrequency_Error,
        "UpAcquisitionPeriodError"              :   Up_AcquisitionPeriod_Error,
        "UpTargetFrequencyRelativeError"        :   Up_TargetFrequency_RelativeError,
        "UpTargetPeriodRelativeError"           :   Up_TargetPeriod_RelativeError,
        "UpAcquisitionFrequencyRelativeError"   :   Up_AcquisitionFrequency_RelativeError,
        "UpAcquisitionPeriodRelativeError"      :   Up_AcquisitionPeriod_RelativeError,
    # round down
        "DownDivider"                           :   DividerDown,
        "DownTargetFrequency"                   :   Down_TargetFrequency_Actual,
        "DownTargetPeriod"                      :   Down_TargetPeriod_Actual,
        "DownAcquisitionFrequency"              :   Down_AcquisitionFrequency_Actual,
        "DownAcquisitionPeriod"                 :   Down_AcquisitionPeriod_Actual,
        "DownTargetFrequencyError"              :   Down_TargetFrequency_Error,
        "DownTargetPeriodError"                 :   Down_TargetPeriod_Error,
        "DownAcquisitionFrequencyError"         :   Down_AcquisitionFrequency_Error,
        "DownAcquisitionPeriodError"            :   Down_AcquisitionPeriod_Error,
        "DownTargetFrequencyRelativeError"      :   Down_TargetFrequency_RelativeError,
        "DownTargetPeriodRelativeError"         :   Down_TargetPeriod_RelativeError,
        "DownAcquisitionFrequencyRelativeError" :   Down_AcquisitionFrequency_RelativeError,
        "DownAcquisitionPeriodRelativeError"    :   Down_AcquisitionPeriod_RelativeError,
    }
    return DividerInfo