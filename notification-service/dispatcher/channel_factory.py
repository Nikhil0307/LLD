from ..channels.email_channel import EmailChannel
from ..channels.sms_channel import SmsChannel
from ..channels.push_channel import PushChannel
from ..base_channel import BaseChannel
from ..notification_model import Channel

class ChannelFactory:
    _channels: dict[Channel, BaseChannel] = {}

    @classmethod
    def get_channel(cls, channel_type: Channel) -> BaseChannel:
        if channel_type not in cls._channels:
            if channel_type == Channel.email:
                cls._channels[channel_type] = EmailChannel()
            elif channel_type == Channel.sms:
                cls._channels[channel_type] = SmsChannel()
            elif channel_type == Channel.push:
                cls._channels[channel_type] = PushChannel()
            else:
                raise ValueError(f"Unsupported channel: {channel_type}")
        return cls._channels[channel_type]
