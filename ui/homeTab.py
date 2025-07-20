from PySide6.QtWidgets import QFileDialog, QCheckBox
from PySide6.QtGui import QImage, QPixmap
from ui.resource import homeTab 
from ui import acg_window
from configurations.settings import logger
import cv2, os, shutil
from configurations.settings import *
import pandas as pd


class HomeTab(homeTab.Ui_MainWindow, acg_window.BaseWindow):

    def __init__(self):
        try:
            super(HomeTab, self).__init__()
            self.setupUi(self)

            self.allCheckboxDone()
            
            self.transactionId = None                                                # contains transactionid
            self.position      = None                                                # contains index like lower, middle, top, bottom
            self.frame_number  = 0                                                   # frame number 1,2,.....,43,44
            self.positionList  = ['Lower', 'Middle', 'Top', 'Bottom']
            self.annotedList   = []                                                  # list of all annoted transactions
            self.zoomFactor    = 0
            self.maxZoom       = 10
            self.scrollArea_border = 9                                               # width of scroll border to be added in scrollAreaWidgetsContent
            self.path = os.getcwd()

            self.hideAllWarning()
            self.pushButton_browse.clicked.connect(self.onBrowse)

            self.pushButton_next_transaction.clicked.connect(self.next_transaction)
            self.pushButton_prev_transaction.clicked.connect(self.previous_transaction)
            self.pushButton_next_position.clicked.connect(self.next_position)
            self.pushButton_prev_position.clicked.connect(self.previous_position)

            self.pushButton_next.clicked.connect(self.onNext)
            self.pushButton_previous.clicked.connect(self.onPrevious)
            
            self.pushButton_ok_files.clicked.connect(lambda : self.saveVideo("OK"))
            self.pushButton_not_ok_files.clicked.connect(lambda : self.saveVideo("NotOk"))

            self.pushButton_zoomIn.clicked.connect(self.zoomIn)
            self.pushButton_zoomOut.clicked.connect(self.zoomOut)
            self.pushButton_reset.clicked.connect(self.reset)

            self.pushButton_close.clicked.connect(self.onClose)

        except Exception as e:
            logger.consoleError("Exception in LoginPage INIT : ", e)

    def hideAllWarning(self):
        self.label_last_ptn_warning.hide()
        self.label_last_txn_warning.hide()
        self.label_pre_ptn_warning.hide()
        self.label_pre_txn_warning.hide()
        self.label_allPostions_warning.hide()
        self.lineEdit_reason.clear()

    # Functio to get the path of transaction folder
    def onBrowse(self):
        try:
            self.frame_number = 0

            file_dialog = QFileDialog()
            file_dialog.setWindowTitle("Select Folder")
            file_dialog.setFileMode(QFileDialog.Directory)
            file_dialog.setOption(QFileDialog.DontUseNativeDialog, False)

            if file_dialog.exec() == 1:
                selected_folders = file_dialog.selectedFiles()
                self.allTransactionsPath = selected_folders[0]
                logger.info(f"Transactions folder path :: {self.allTransactionsPath}")
                self.label_File_path.setText(self.allTransactionsPath)

            # Make a list of all annoted folders and update it 
            self.annotedList = os.listdir(self.path+"/Outputs/Annoted")
            self.next_transaction()

        except Exception as e:
            logger.consoleError("Exception in onBrowse : ", e)

    # Functions to traverse transaction and indexes
    def next_transaction(self):
        try:
            # Move to next position only if all or no index have been completed
            result = self.allCheckboxDone()
            if result:
                self.hideAllWarning()

                # get list of folders in transactions and already annoted folders
                allTransactions = os.listdir(self.allTransactionsPath)
                allTransactions.sort()
                self.annotedList = os.listdir(self.path+"/Outputs/Annoted")

                # convert the list of folders in transactions, from current transaction to last transaction
                if self.transactionId == None:
                    pass
                else:
                    index = allTransactions.index(self.transactionId)
                    allTransactions = [allTransactions[i] for i in range(index+1, len(allTransactions))]

                logger.info(f"\nNEXT Transactions :: {allTransactions}, Already annoted :: {self.annotedList}")
                for folder_name in allTransactions:
                    folder_path = os.path.join(self.allTransactionsPath, folder_name)
                    
                    # Only check directories (folders)
                    if os.path.isdir(folder_path):
                        logger.info(f"Current Transactions :: {folder_name}")
                        if folder_name not in self.annotedList:
                            self.transactionId = folder_name
                            self.label_frame_transaction.setText(str(self.transactionId))
                            self.position = 'Lower'
                            self.label_frame_position.setText(str(self.position))
                            self.processVideo(self.allTransactionsPath+"/"+self.transactionId+"/"+self.position)
                            return
                self.label_last_txn_warning.show()
            else:
                self.label_allPostions_warning.show()

            
        except Exception as e:
             logger.consoleError("Exception in next_transaction : ", e)

    def previous_transaction(self):
        try:
            # Move to next position only if all or no index have been completef
            result = self.allCheckboxDone()
            if result:
                self.hideAllWarning()

                # get list of folders in transactions and already annoted folders
                allTransactions = os.listdir(self.allTransactionsPath)
                allTransactions.sort()
                self.annotedList = os.listdir(self.path+"/Outputs/Annoted")

                # convert the list of folders in transactions, from current transaction to first transaction
                if self.transactionId == None:
                    pass
                else:
                    index = allTransactions.index(self.transactionId)
                    allTransactions = [allTransactions[i] for i in range(index-1, -1, -1)]

                # List all directories in the provided directory
                logger.info(f"\nPREVIOUS Transactions :: {allTransactions}, Already annoted :: {self.annotedList}")
                for folder_name in allTransactions:
                    folder_path = os.path.join(self.allTransactionsPath, folder_name)
                    
                    # Only check directories (folders)
                    if os.path.isdir(folder_path):
                        logger.info(f"Current Transactions :: {folder_name}, Already annoted :: {self.annotedList}")
                        if folder_name not in self.annotedList:
                            self.transactionId = folder_name
                            self.label_frame_transaction.setText(str(self.transactionId))
                            self.position = 'Lower'
                            self.label_frame_position.setText(str(self.position))
                            self.processVideo(self.allTransactionsPath+"/"+self.transactionId+"/"+self.position)
                            return
                self.label_pre_txn_warning.show()
            else:
                self.label_allPostions_warning.show()
            
        except Exception as e:
             logger.consoleError("Exception in previous_transaction : ", e)

    def next_position(self):
        try:
            self.hideAllWarning()

            # check if next position exists then change position
            current_index = self.positionList.index(self.position)
            if current_index + 1 < len(self.positionList):
                next_index = current_index + 1
                self.position = self.positionList[next_index]
                self.processVideo(self.allTransactionsPath+"/"+self.transactionId+"/"+self.position)
            else:
                next_index = current_index
                self.label_last_ptn_warning.show()

            self.position = self.positionList[next_index]
            logger.info(f"Current Index :: {self.position}")
            self.label_frame_position.setText(str(self.position))

        except Exception as e:
             logger.consoleError("Exception in next_position : ", e)

    def previous_position(self):
        try:
            self.hideAllWarning()

            # check if previous position exists then change position
            current_index = self.positionList.index(self.position)
            if current_index - 1 >= 0:
                prev_index = current_index - 1
                self.position = self.positionList[prev_index]
                self.processVideo(self.allTransactionsPath+"/"+self.transactionId+"/"+self.position)
            else:
                prev_index = current_index
                self.label_pre_ptn_warning.show()
            
            logger.info(f"Current Index :: {self.position}")
            self.label_frame_position.setText(str(self.position))
            
        except Exception as e:
             logger.consoleError("Exception in previous_position : ", e)

    # Function to convert Video to frames
    def processVideo(self, video_path):
        try:
            logger.info(f"------------------------------processVideo at path------------------------------{video_path}")
            self.video_name = os.listdir(video_path)[0]
            self.video_path = os.path.join(video_path, self.video_name)
            cap = cv2.VideoCapture(self.video_path)

            if not cap.isOpened():
                logger.info("Error: Could not open video.")
                return [] 
            
            self.allFrames = []
            self.frame_count = 0

            while True:
                ret, frame = cap.read()
                # If frame reading was successful
                if ret:
                    self.allFrames.append(frame)  # Append the frame to the list
                    self.frame_count += 1
                else:
                    break  # Break when no more frames are left
            
            cap.release()  # Release the video capture object
            logger.info(f"Extracted {self.frame_count} frames.")
            self.label_frame_count.setText(str(self.frame_count))
            self.frame_number = 0
            self.displayFrame(self.allFrames[self.frame_number])
        except Exception as e:
             logger.consoleError("Exception in processVideo : ", e)

    # Function to display particular frame
    def displayFrame(self, frame):
        try:
            self.reset()

            self.label_frame_number.setText(str(self.frame_number+1))

            # Convert frame (which is a NumPy array) to QImage
            height, width, channels = frame.shape
            self.original_width = width
            self.original_height = height
            bytes_per_line = channels * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_BGR888)

            # Convert QImage to QPixmap and display it in QLabel
            pixmap = QPixmap.fromImage(q_image)
            self.original_image = pixmap
            self.label.setPixmap(self.original_image)

        except Exception as e:
             logger.consoleError("Exception in displayFrame : ", e)

    # Functions to traverse Images
    def onNext(self):
        try:
            if self.frame_number+1 < self.frame_count:
                self.frame_number += 1
                print(f"Index {self.frame_number}, Frame {self.frame_number+1}")
                self.label_frame_number.setText(str(self.frame_number+1))
                self.displayFrame(self.allFrames[self.frame_number])

        except Exception as e:
             logger.consoleError("Exception in onNext : ", e)

    def onPrevious(self):
        try:
            if self.frame_number > 0:
                self.frame_number -= 1
                print(f"Index {self.frame_number}, Frame {self.frame_number+1}")
                self.label_frame_number.setText(str(self.frame_number+1))
                self.displayFrame(self.allFrames[self.frame_number])

        except Exception as e:
             logger.consoleError("Exception in onPrevious : ", e)

    def saveVideo(self, folder):
        try:
            logger.info(f"------------------------------saveVideo------------------------------")
            source = self.allTransactionsPath+"/"+self.transactionId+"/"+self.position
            destination = os.getcwd()+"/Outputs/Annoted/"+self.transactionId+"/"+folder+"/"+self.position
            logger.info(f"Source :: {source}, Destination :: {destination}")

            if not os.path.isdir(destination):
                os.makedirs(destination, exist_ok=True)

                # Copy video from source to destination
                shutil.copytree(source, destination, dirs_exist_ok=True)

                # Mark the checkboxes after saving video
                if self.position=="Lower":
                    self.checkBox_lower.setChecked(True)
                elif self.position=="Middle":
                    self.checkBox_middle.setChecked(True)
                elif self.position=="Top":
                    self.checkBox_top.setChecked(True)
                else:
                    self.checkBox_bottom.setChecked(True)

                # Save CSV file of results
                reason = self.lineEdit_reason.text()
                results = [{"Tid":self.transactionId,"Index":self.position,"Reason":reason}]
                results_path="Outputs/Results.csv"
                df2 = pd.DataFrame(results,dtype=object)
                df2.to_csv(results_path, mode='a', header=not os.path.exists(results_path), index=False)
            else:
                logger.info("Already Saved")
        except Exception as e:
             logger.consoleError("Exception in saveVideo : ", e)

    def allCheckboxDone(self):
        allCombobox = self.frame.findChildren(QCheckBox)
        count=0
        for comboBox in allCombobox:
            if comboBox.isChecked()==True:
                count+=1
        if count==0 or count==4:
            self.checkBox_lower.setChecked(False)
            self.checkBox_middle.setChecked(False)
            self.checkBox_top.setChecked(False)
            self.checkBox_bottom.setChecked(False)
            return True
        else:
            return False

    # Image control Functions
    def zoomIn(self):
        try:
            self.zoomFactor = self.zoomFactor+1 if self.zoomFactor<self.maxZoom else self.zoomFactor
            self.setGeometry()
        except Exception as e:
            logger.consoleError("Exception in reset : ", e)

    def reset(self):
        try:
            self.zoomFactor = 0
            self.setGeometry()
        except Exception as e:
            logger.consoleError("Exception in reset : ", e)

    def zoomOut(self):
        try:
            self.zoomFactor = self.zoomFactor-1 if self.zoomFactor>0 else self.zoomFactor
            self.setGeometry()
        except Exception as e:
            logger.consoleError("Exception in reset : ", e)    

    def setGeometry(self):
        self.label.setFixedHeight(700+(self.zoomFactor*100))
        self.label.setFixedWidth(700+(self.zoomFactor*100))
        self.scrollAreaWidgetContents.setMinimumHeight(700+self.scrollArea_border+(self.zoomFactor*100))
        self.scrollAreaWidgetContents.setMinimumWidth(700+self.scrollArea_border+(self.zoomFactor*100))

    def onClose(self):
        self.deleteLater()
        self.close()