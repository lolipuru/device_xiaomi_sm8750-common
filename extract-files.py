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
        'libc++_shared',
        'libmialgo',
        'vendor.qti.hardware.display.config-V12-ndk', # TEMP
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
     (
       'vendor/lib64/libsxrservice.so'
     ): blob_fixup()
        .replace_needed(
            'android.hardware.common-V2-ndk_platform.so',
            'android.hardware.common-V2-ndk.so'
        )

        .replace_needed(
            'android.hardware.audio.core-V2-ndk.so',
            'android.hardware.audio.core-V3-ndk.so'
        )

        .replace_needed(
            'android.media.audio.common.types-V3-ndk.so',
            'android.media.audio.common.types-V4-ndk.so'
        ),
     (
       'odm/bin/hw/vendor.xiaomi.hw.touchfeature-service',
       'odm/bin/hw/vendor.xiaomi.sensor.citsensorservice.aidl',
       'odm/lib64/hw/displayfeature.default.so',
       'odm/lib64/libadaptivehdr.so',
       'odm/lib64/libcolortempmode.so',
       'odm/lib64/libdither.so',
       'odm/lib64/libflatmode.so',
       'odm/lib64/libhistprocess.so',
       'odm/lib64/libmiBrightness.so',
       'odm/lib64/libmiSensorCtrl.so',
       'odm/lib64/libpaperMode.so',
       'odm/lib64/librhytheyecare.so',
       'odm/lib64/libsdr2hdr.so',
       'odm/lib64/libsre.so',
       'odm/lib64/libtruetone.so',
       'odm/lib64/libvideomode.so',
       'vendor/lib64/libgnss.so',
     ): blob_fixup()
        .replace_needed(
            'android.hardware.sensors-V2-ndk.so',
            'android.hardware.sensors-V3-ndk.so'
        ),
    (
        'vendor/lib64/hw/libaudiocorehal.qti.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.audio.effect-V2-ndk.so',
            'android.hardware.audio.effect-V3-ndk.so'
        )

        .replace_needed(
            'android.hardware.audio.core-V2-ndk.so',
            'android.hardware.audio.core-V3-ndk.so'
        )

        .replace_needed(
            'android.media.audio.common.types-V3-ndk.so',
            'android.media.audio.common.types-V4-ndk.so'
        )

        .replace_needed(
            'android.hardware.audio.core.sounddose-V1-ndk.so',
            'android.hardware.audio.core.sounddose-V3-ndk.so'
        ),
    (
       'vendor/lib64/hw/libaudioeffecthal.qti.so',
       'vendor/lib64/libswspatializeraidl_ext.so',
       'vendor/lib64/soundfx/libbundleaidl.so',
       'vendor/lib64/soundfx/libdlbvolaidl.so',
       'vendor/lib64/soundfx/libdownmixaidl.so',
       'vendor/lib64/soundfx/libdynamicsprocessingaidl.so',
       'vendor/lib64/soundfx/libhwdapaidl.so',
       'vendor/lib64/soundfx/libloudnessenhanceraidl.so',
       'vendor/lib64/soundfx/libmiwndnsprocessingaidl.so',
       'vendor/lib64/soundfx/libreverbaidl.so',
       'vendor/lib64/soundfx/libswgamedapaidl.so',
       'vendor/lib64/soundfx/libswspatializeraidl.so',
       'vendor/lib64/soundfx/libvisualizeraidl.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.audio.effect-V2-ndk.so',
            'android.hardware.audio.effect-V3-ndk.so'
        ),
    (
       'vendor/lib64/libaudioplatformconverter.qti.so',
       'vendor/lib64/libqtigefar.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.audio.core-V2-ndk.so',
            'android.hardware.audio.core-V3-ndk.so'
        )

        .replace_needed(
            'android.media.audio.common.types-V3-ndk.so',
            'android.media.audio.common.types-V4-ndk.so'
        ),
    (
       'vendor/lib64/libmisoundfx_aidl_ext.so',
       'vendor/lib64/soundfx/libquasar.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.audio.effect-V2-ndk.so',
            'android.hardware.audio.effect-V3-ndk.so'
        )

        .replace_needed(
            'android.media.audio.common.types-V3-ndk.so',
            'android.media.audio.common.types-V4-ndk.so'
        ),
    (
        'vendor/lib64/soundfx/libspatializeraidl.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.audio.effect-V2-ndk.so',
            'android.hardware.audio.effect-V3-ndk.so'
        )

        .replace_needed(
            'android.hardware.audio.core-V2-ndk.so',
            'android.hardware.audio.core-V3-ndk.so'
        )

        .replace_needed(
            'android.media.audio.common.types-V3-ndk.so',
            'android.media.audio.common.types-V4-ndk.so'
        ),
    (
       'vendor/lib64/hw/libaudiocorehal.default.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.audio.core-V2-ndk.so',
            'android.hardware.audio.core-V3-ndk.so'
        )

        .replace_needed(
            'android.media.audio.common.types-V3-ndk.so',
            'android.media.audio.common.types-V4-ndk.so'
        ),
    (
       'vendor/lib64/libwfdmmsrc_proprietary.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.audio.core-V2-ndk.so',
            'android.hardware.audio.core-V3-ndk.so'
        )

        .replace_needed(
            'android.media.audio.common.types-V2-ndk.so',
            'android.media.audio.common.types-V4-ndk.so'
        ),
    (
       'vendor/lib64/hw/android.hardware.bluetooth.audio_sw.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.bluetooth.audio-V4-ndk.so',
            'android.hardware.bluetooth.audio-V5-ndk.so'
        )

        .replace_needed(
            'android.hardware.audio.core-V2-ndk.so',
            'android.hardware.audio.core-V3-ndk.so'
        ),
    (
       'vendor/lib64/btaudio_offload_if.so',
       'vendor/lib64/hw/android.hardware.bluetooth.audio-impl-qti.so',
       'vendor/lib64/hw/audio.bluetooth_qti.default.so',
       'vendor/lib64/libbluetooth_audio_session_aidl_qti.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.bluetooth.audio-V4-ndk.so',
            'android.hardware.bluetooth.audio-V5-ndk.so'
        ),
    (
       'vendor/bin/hw/vendor.qti.hardware.display.composer-service',
    ): blob_fixup()
        .replace_needed(
            'vendor.qti.hardware.display.composer3-V1-ndk.so',
            'vendor.qti.hardware.display.composer3-V3-ndk.so'
        ),
    (
       'vendor/lib64/libqcodec2_core.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.graphics.common-V5-ndk.so',
            'android.hardware.graphics.common-V6-ndk.so'
        )
        .add_needed('libcodec2_shim.so'),
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