#
# Copyright (C) 2024 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

LOCAL_PATH := $(call my-dir)

ifneq ($(filter dada haotian xuanyuan miro,$(TARGET_DEVICE)),)
	include $(call all-makefiles-under,$(LOCAL_PATH))
	include $(CLEAR_VARS)

endif