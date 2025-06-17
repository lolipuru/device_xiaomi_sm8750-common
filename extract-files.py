#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/sm8750-common',
    'hardware/qcom-caf/wlan',
    'hardware/qcom-caf/sm8750',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}-{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'android.media.audio.common.types-V6-ndk'
    ): lib_fixup_vendor_suffix,
    (
        'libagmclient',
        'libagmmixer',
        'libc++_shared',
        'libmialgo',
        'libsndcardparser',
        'android.hardware.audio.common-V3-ndk',
        'android.hardware.audio.core-V2-ndk',
        'android.hardware.audio.core.sounddose-V1-ndk',
        'android.hardware.audio.effect-V2-ndk',
        'android.hardware.bluetooth.audio-V4-ndk',
        'android.hardware.common-V2-ndk',
        'android.hardware.graphics.common-V5-ndk',
        'android.hardware.graphics.composer3-V3-ndk',
        'android.hardware.sensors-V2-ndk',
        'android.media.audio.common.types-V3-ndk',
        'vendor.qti.hardware.display.composer3-V1-ndk',
        'vendor.qti.hardware.display.config-V12-ndk'
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
}  # fmt: skip

module = ExtractUtilsModule(
    'sm8750-common',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()